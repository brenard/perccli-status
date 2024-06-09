"""perccli_status tests"""

from pathlib import Path
from subprocess import CompletedProcess
from unittest.mock import Mock, patch

from perccli_status import main as perccli_status_main


TESTS_DIR = Path(__file__).resolve().parent


def test_run():
    """test run"""

    percclimock = Mock(
        side_effect=[
            CompletedProcess(
                args=[],
                returncode=0,
                stdout=Path(f"{TESTS_DIR}/{item}").read_text(encoding="utf-8"),
            )
            for item in [
                "output-ok-controllers.json",
                "output-ok-vdisks.json",
                "output-ok-disks.json",
            ]
        ]
    )

    with patch("subprocess.run", percclimock):
        ret = perccli_status_main([])
        assert ret == 0


def test_run_nagios():
    """test run"""

    percclimock = Mock(
        side_effect=[
            CompletedProcess(
                args=[],
                returncode=0,
                stdout=Path(f"{TESTS_DIR}/{item}").read_text(encoding="utf-8"),
            )
            for item in [
                "output-ok-controllers.json",
                "output-ok-vdisks.json",
                "output-ok-disks.json",
            ]
        ]
    )

    with patch("subprocess.run", percclimock):
        ret = perccli_status_main(["--nagios"])
        assert ret == 0


def test_jsonfail():
    """test err json"""

    percclimock = Mock(
        return_value=CompletedProcess(
            args=[],
            returncode=0,
            stdout="notjson",
        )
    )

    with patch("subprocess.run", percclimock):
        ret = perccli_status_main([])
        assert ret == 2


def test_fails():
    """test error detections"""

    percclimock = Mock(
        side_effect=[
            CompletedProcess(
                args=[],
                returncode=0,
                stdout=Path(f"{TESTS_DIR}/{item}").read_text(encoding="utf-8"),
            )
            for item in [
                "output-fail-controllers.json",
                "output-fail-vdisks.json",
                "output-fail-disks.json",
            ]
        ]
    )

    with patch("subprocess.run", percclimock):
        ret = perccli_status_main([])
        assert ret == 2
