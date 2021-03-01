import json
from pathlib import Path

import pytest
from pydantic import Extra, create_model_from_typeddict


@pytest.fixture
def samples_dir():
    return Path(__file__).parent.parent / "samples"


@pytest.fixture
def sample_json(request, samples_dir):
    file_name = request.param

    with open(samples_dir / file_name) as f:
        return json.load(f)


@pytest.fixture
def pydantic_model(request):
    typed_dict_obj = request.param

    class Config:
        extra = Extra.forbid

    return create_model_from_typeddict(
        typed_dict_obj,
        __config__=Config,
    )
