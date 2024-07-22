#
# Copyright 2024 Canonical, Ltd.
#

import pytest
from k8s_test_harness.util import docker_util, env_util


@pytest.mark.parametrize("image_version", ("1.24.0", "1.27.2"))
def test_sanity(image_version):
    rock = env_util.get_build_meta_info_for_rock_version(
        "cluster-autoscaler", image_version, "amd64"
    )
    image = rock.image

    entrypoint = "/cluster-autoscaler"
    # assert we have the expected files
    process = docker_util.run_in_docker(image, [entrypoint, "--help"])
    assert "Usage of /cluster-autoscaler:" in process.stderr
