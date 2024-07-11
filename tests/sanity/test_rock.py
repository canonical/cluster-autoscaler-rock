import subprocess
import os


def test_sanity():
    image_variable = "ROCK_CLUSTER_AUTOSCALER"
    entrypoint = "/cluster-autoscaler"
    image = os.getenv(image_variable)
    assert image is not None, f"${image_variable} is not set"
    # assert we have the expected files
    asd = subprocess.run(
        ["docker", "run", "--rm", "--entrypoint", entrypoint, image, "--help"],
        capture_output=True,
        text=True
    )
    assert "Usage of /cluster-autoscaler:" in asd.stderr
