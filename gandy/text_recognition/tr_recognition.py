import albumentations as A
import numpy as np

from gandy.text_recognition.base_text_recognition import BaseTextRecognition
import albumentations as A
import numpy as np
from gandy.onnx_models.tr_ocr import OnnxVision
import logging
logger = logging.getLogger('Gandy')

class TrOCRTextRecognitionApp(BaseTextRecognition):
    def __init__(self, model_sub_path = '/', has_proj = True):
        super().__init__(preload=False) # NOTE: Preload was enabled for testing. Can re-enable later if needed.

        self.transform = A.Compose([
            # NOTE: Currently worse with these two, but may do well in the future.
            # NOTE: Default border mode of reflect101 is VERY bad. CONSTANT border performs way better.
            ## A.LongestMaxSize(224, always_apply=True),
            ## A.PadIfNeeded(224, 224, border_mode=cv2.BORDER_CONSTANT),
            A.ToGray(always_apply=True),
        ])

        self.model_sub_path = model_sub_path
        self.has_proj = has_proj

    def load_model(self):
        s = self.model_sub_path

        logger.info('Loading object recognition model...')
        self.model = OnnxVision(
            f'models/minocr{s}encoder.onnx', f'models/minocr{s}decoder.onnx', f'models/minocr{s}decoder_init.onnx', f'models/minocr{s}proj.onnx' if self.has_proj else None,
            f'models/minocr{s}minocr_tokenizer', f'models/minocr{s}minocr_feature_extractor', f'models/minocr{s}minocr_config',
            use_cuda=self.use_cuda,
        )
        logger.info('Done loading object recognition model!')

        return super().load_model()

    def process_one_image(self, cropped_image):
        augmented = self.transform(image=cropped_image)
        cropped_image = augmented['image']

        output = self.model.full_pipe(cropped_image)
        return output

    def process(self, image, i_frames):
        for i_frame in i_frames:
            for bbox in i_frame.speech_bboxes:
                cropped_image = image.crop(bbox)

                cropped_image = np.array(cropped_image)

                logger.debug(f'Scanning a text region... - IMG SHAPE: {cropped_image.shape}')
                text = self.process_one_image(cropped_image)
                logger.debug(f'Done scanning a text region! - IMG SHAPE: {cropped_image.shape}')
                logger.debug(f'Found text: {text}')

                i_frame.add_untranslated_speech_text(text)

        return i_frames
