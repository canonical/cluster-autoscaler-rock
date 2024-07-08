
import random
import pytest
import string
import subprocess

from charmed_kubeflow_chisme.rock import CheckRock


@pytest.fixture()
def rock_test_env(tmpdir):
    """Yields a temporary directory and random docker container name, then cleans them up after."""
    container_name = "".join(
        [str(i) for i in random.choices(string.ascii_lowercase, k=8)]
    )
    yield tmpdir, container_name

    try:
        subprocess.run(["docker", "rm", container_name])
    except Exception:
        pass
    # tmpdir fixture we use here should clean up the other files for us


def test_rock():
    """Test rock."""
    check_rock = CheckRock("rockcraft.yaml")
    rock_image = check_rock.get_name()
    rock_version = check_rock.get_version()
    LOCAL_ROCK_IMAGE = f"{rock_image}:{rock_version}"
    # assert we have the expected files
    asd = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--entrypoint",
            "/cluster-autoscaler",
            LOCAL_ROCK_IMAGE,
            "--help"
        ],
        capture_output=True,
        text=True
    )
    assert "Usage of /cluster-autoscaler:" in asd.stderr
