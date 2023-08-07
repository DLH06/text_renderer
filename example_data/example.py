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

font_cfg_mya = dict(
    font_dir=FONT_DIR / "mya",
    font_list_file=FONT_LIST_DIR / "mya_font_list.txt",
    font_size=(20, 31),
)
font_cfg_en = dict(
    font_dir=FONT_DIR / "en",
    font_list_file=FONT_LIST_DIR / "en_font_list.txt",
    font_size=(20, 31),
)

perspective_transform = NormPerspectiveTransformCfg(20, 20, 1.5)


def base_cfg_id(
    name: str, corpus, corpus_effects=None, layout_effects=None, layout=None, gray=False
):
    return GeneratorCfg(
        num_image=15000,
        save_dir=OUT_DIR / name,
        render_cfg=RenderCfg(
            bg_dir=DATA_DIR / "bg_test",
            perspective_transform=perspective_transform,
            gray=gray,
            layout_effects=layout_effects,
            layout=layout,
            corpus=corpus,
            corpus_effects=corpus_effects,
        ),
    )
def base_cfg(
    name: str, corpus, corpus_effects=None, layout_effects=None, layout=None, gray=False
):
    return GeneratorCfg(
        num_image=15000,
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
def base_cfg_en(
    name: str, corpus, corpus_effects=None, layout_effects=None, layout=None, gray=False
):
    return GeneratorCfg(
        num_image=77370, # english
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
def base_cfg_mya(
    name: str, corpus, corpus_effects=None, layout_effects=None, layout=None, gray=False
):
    return GeneratorCfg(
        num_image=135680, # myanmar
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

def enum_data_en():
    return base_cfg_en(
        inspect.currentframe().f_code.co_name,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "en_ocr.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "new.txt",
                **font_cfg_en
            ),
        ),
        corpus_effects=Effects(
            [
                Line(
                    0.15,
                    thickness=(1, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.05, 0.55], center=False),
                ImgAugEffect(
                    p=0.15,
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
def enum_data_mya():
    return base_cfg_mya(
        inspect.currentframe().f_code.co_name,
        corpus=EnumCorpus(
            EnumCorpusCfg(
                text_paths=[TEXT_DIR / "mya_ocr.txt"],
                filter_by_chars=True,
                chars_file=CHAR_DIR / "new.txt",
                **font_cfg_mya
            ),
        ),
        corpus_effects=Effects(
            [
                Line(
                    0.15,
                    thickness=(1, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.05, 0.55], center=False),
                ImgAugEffect(
                    p=0.15,
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


def same_line_data_1():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=SameLineLayout(),
        gray=False,
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    # text_paths=[TEXT_DIR / "enum_text.txt"],
                    items=["အမှတ်"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "gen_base/mya_id_full.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
        ],
    )
def same_line_data_2():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=SameLineLayout(),
        gray=False,
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    # text_paths=[TEXT_DIR / "enum_text.txt"],
                    items=["အမှတ်"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "gen_base/mya_id_part_1.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "gen_base/mya_id_part_2.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
        ],
    )
def same_line_data_id():
    return base_cfg_id(
        inspect.currentframe().f_code.co_name,
        layout=SameLineLayout(),
        gray=False,
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "gen_base/mya_id_part_1.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[TEXT_DIR / "gen_base/mya_id_part_2.txt"],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "new.txt",
                    **font_cfg_mya
                ),
            ),
        ],
        corpus_effects=[Effects(
            [
                Line(
                    0.15,
                    thickness=(1, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.05, 0.55], center=False),
                ImgAugEffect(
                    p=0.15,
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
        ), Effects(
            [
                Line(
                    0.15,
                    thickness=(1, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.05, 0.55], center=False),
                ImgAugEffect(
                    p=0.15,
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
        )]
    )


def extra_text_line_data_en_en():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=ExtraTextLineLayout(),
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "en_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    font_dir=font_cfg_en["font_dir"],
                    font_list_file=font_cfg_en["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "en_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    font_dir=font_cfg_en["font_dir"],
                    font_list_file=font_cfg_en["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
        ],
        corpus_effects=[Effects(
            [
                Line(
                    0.15,
                    thickness=(2, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                # Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.1, 0.75], center=True),
                ImgAugEffect(
                    p=1,
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
            ]), NoEffects()],
    )
def extra_text_line_data_en_mya():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=ExtraTextLineLayout(),
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "en_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg_en["font_dir"],
                    font_list_file=font_cfg_en["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "mya_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg_mya["font_dir"],
                    font_list_file=font_cfg_mya["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
        ],
        corpus_effects=[Effects(
            [
                Line(
                    0.15,
                    thickness=(2, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                # Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.1, 0.75], center=True),
                ImgAugEffect(
                    p=1,
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
            ]), NoEffects()],
    )
def extra_text_line_data_mya_mya():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=ExtraTextLineLayout(),
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "mya_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg_mya["font_dir"],
                    font_list_file=font_cfg_mya["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "mya_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg_mya["font_dir"],
                    font_list_file=font_cfg_mya["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
        ],
        corpus_effects=[Effects(
            [
                Line(
                    0.15,
                    thickness=(2, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                # Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.1, 0.75], center=True),
                ImgAugEffect(
                    p=1,
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
            ]), NoEffects()],
    )
def extra_text_line_data_mya_en():
    return base_cfg(
        inspect.currentframe().f_code.co_name,
        layout=ExtraTextLineLayout(),
        corpus=[
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "mya_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg_mya["font_dir"],
                    font_list_file=font_cfg_mya["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
            EnumCorpus(
                EnumCorpusCfg(
                    text_paths=[
                        TEXT_DIR / "en_ocr.txt",
                    ],
                    filter_by_chars=True,
                    chars_file=CHAR_DIR / "mya_chars.txt",
                    # length=(9, 10),
                    font_dir=font_cfg_en["font_dir"],
                    font_list_file=font_cfg_en["font_list_file"],
                    font_size=(20, 31),
                ),
            ),
        ],
        corpus_effects=[Effects(
            [
                Line(
                    0.15,
                    thickness=(2, 3),
                    line_pos_p=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
                    # top, bottom, left, right, top_left, top_right, bottom_left, bottom_right, horizontal_middle, vertical_middle
                ),
                # Padding(p=0.15, w_ratio=[0.05, 0.25], h_ratio=[0.1, 0.75], center=True),
                ImgAugEffect(
                    p=1,
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
            ]), NoEffects()],
    )


# fmt: off
# The configuration file must have a configs variable
configs = [
    # enum_data_en(),
    # enum_data_mya(),
    
    # same_line_data_1(),
    # same_line_data_2(),
    same_line_data_id(),

    # extra_text_line_data_en_mya(),
    # extra_text_line_data_en_en(),
    # extra_text_line_data_mya_en(),
    # extra_text_line_data_mya_mya(),
]
# fmt: on
