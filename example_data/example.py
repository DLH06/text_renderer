import inspect
import os
from pathlib import Path
import imgaug.augmenters as iaa

from text_renderer.effect import *
from text_renderer.corpus import *
from text_renderer.config import (
    RenderCfg,
    NormPerspectiveTransformCfg,
    GeneratorCfg,
    FixedTextColorCfg,
)
from text_renderer.layout.same_line import SameLineLayout
from text_renderer.layout.extra_text_line import ExtraTextLineLayout


CURRENT_DIR = Path(os.path.abspath(os.path.dirname(__file__)))
OUT_DIR = CURRENT_DIR / "output"
DATA_DIR = CURRENT_DIR
BG_DIR = DATA_DIR / "bg"
CHAR_DIR = DATA_DIR / "char"
FONT_DIR = DATA_DIR / "font"
FONT_LIST_DIR = DATA_DIR / "font_list"
TEXT_DIR = DATA_DIR / "text"

font_cfg = dict(
    # font_dir=FONT_DIR / "en",
    # font_list_file=FONT_LIST_DIR / "en_font_list.txt",
    font_dir=FONT_DIR / "mya",
    font_list_file=FONT_LIST_DIR / "mya_font_list.txt",
    font_size=(20, 31),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)


def get_char_corpus():
    return CharCorpus(
        CharCorpusCfg(
            text_paths=[TEXT_DIR / "mya_text.txt"],
            filter_by_chars=True,
            chars_file=CHAR_DIR / "mya_chars.txt",
            length=(5, 10),
            char_spacing=(-0.3, 1.3),
            **font_cfg
        ),
    )


def base_cfg(
    name: str, corpus, corpus_effects=None, layout_effects=None, layout=None, gray=False
):
    return GeneratorCfg(
        # num_image=16223, # myanmar
        # num_image=6012, # english
        num_image=10,
        save_dir=OUT_DIR / name,
        render_cfg=RenderCfg(
            bg_dir=BG_DIR,
            perspective_transform=perspective_transform,
            gray=gray,
            layout_effects=layout_effects,
            layout=layout,
            corpus=corpus,
            corpus_effects=corpus_effects,
        ),
    )


def chn_data():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_char_corpus(),
        corpus_effects=Effects(
            [
                Line(0.5, color_cfg=FixedTextColorCfg()),
                OneOf([DropoutRand(), DropoutVertical()]),
            ]
        ),
    )


def enum_data():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                # text_paths=[TEXT_DIR / "en/en_ocr.txt"],
                text_paths=[TEXT_DIR / "mya/mya_ocr.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "mya_chars.txt",
                **font_cfg
            ),
        ),
        corpus_effects=Effects(
            [
                Line(
                    0.2,
                    thickness=(2, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                Padding(p=0.1, w_ratio=[0.2, 0.21], h_ratio=[0.7, 0.71], center=True),
                ImgAugEffect(
                    p=0.1,
                    aug=iaa.SomeOf(
                        (1, 2),
                        [
                            iaa.Emboss(alpha=0.15, strength=(1.2, 1.3)),
                            iaa.OneOf([
                                iaa.GaussianBlur((0.5, 1.1)),
                                iaa.AverageBlur(k=(2, 3)),
                                iaa.MotionBlur(k=4),
                                iaa.MedianBlur(k=(1, 3)),
                            ]),
                            iaa.OneOf([
                                iaa.pillike.Autocontrast((10, 20), per_channel=True),
                                iaa.pillike.EnhanceColor(),
                                iaa.pillike.EnhanceSharpness(),
                                iaa.pillike.FilterEdgeEnhanceMore(),
                            ]),
                            iaa.OneOf(
                                [
                                    iaa.Dropout(0.3, per_channel=0.5),
                                    iaa.SaltAndPepper(0.3, per_channel=True),
                                    iaa.Invert(0.5),
                                    iaa.AdditiveGaussianNoise(scale=(0.1, 0.2*255))
                                ]
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )


def rand_data():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=RandCorpus(
            RandCorpusCfg(chars_file=CHAR_DIR / "chn.txt", **font_cfg),
        ),
    )


def eng_word_data():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=WordCorpus(
            WordCorpusCfg(
                text_paths=[TEXT_DIR / "eng_text.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "eng.txt",
                **font_cfg
            ),
        ),
    )


def same_line_data():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=SameLineLayout(),
        gray=False,
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "enum_text.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "chn.txt",
                    **font_cfg
                ),
            ),
            CharCorpus(
                CharCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "chn_text.txt",
                        TEXT_DIR / "eng_text.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "chn.txt",
                    length=(5, 10),
                    font_dir=font_cfg["font_dir"],
                    font_list_file=font_cfg["font_list_file"],
                    font_size=(30, 35),
                ),
            ),
        ],
        corpus_effects=[Effects([Padding(), DropoutRand()]), NoEffects()],
        layout_effects=Effects(Line(p=1)),
    )


def extra_text_line_data():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=ExtraTextLineLayout(),
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        # TEXT_DIR / "en/en_ocr.txt",
                        TEXT_DIR / "mya/mya_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg["font_dir"],
                    font_list_file=font_cfg["font_list_file"],
                    font_size=(30, 31),
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        # TEXT_DIR / "en/en_ocr.txt",
                        TEXT_DIR / "mya/mya_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg["font_dir"],
                    font_list_file=font_cfg["font_list_file"],
                    font_size=(30, 31),
                ),
            ),
        ],
        corpus_effects=[Effects([
            Line(
                    0.1,
                    thickness=(2, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
            # Padding(p=0.1, w_ratio=[0.2, 0.21], h_ratio=[0.7, 0.71], center=True),
            ImgAugEffect(
                p=1,
                aug=iaa.SomeOf(
                    (1, 2),
                    [
                        iaa.Emboss(alpha=0.15, strength=(1.2, 1.3)),
                        iaa.GaussianBlur((1, 1.5)),
                        iaa.OneOf(
                            [
                                iaa.Dropout(0.3, per_channel=0.5),
                                iaa.SaltAndPepper(0.3, per_channel=True),
                            ]
                        ),
                    ],
                ),
            ),
        ]), NoEffects()],
        # layout_effects=Effects(Line(p=1)),
    )


def imgaug_emboss_example():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        corpus=get_char_corpus(),
        corpus_effects=Effects(
            [
                Padding(p=1, w_ratio=[0.2, 0.21], h_ratio=[0.7, 0.71], center=True),
                ImgAugEffect(aug=iaa.Emboss(alpha=(0.9, 1.0), strength=(1.5, 1.6))),
            ]
        ),
    )


# fmt: off
# The configuration file must have a configs variable
configs = [
    # chn_data(),
    enum_data(),
    # rand_data(),
    # eng_word_data(),
    # same_line_data(),
    # extra_text_line_data(),
    # imgaug_emboss_example()
]
# fmt: on
