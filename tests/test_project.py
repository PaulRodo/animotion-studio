from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectFilesTest(unittest.TestCase):
    def test_html_and_server_exist(self):
        self.assertTrue((ROOT / "index.html").is_file())
        self.assertTrue((ROOT / "run_server.py").is_file())

    def test_no_heavy_wan_start_recommendation(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("RTX 2050", html)
        self.assertNotIn("выбери <b>Wan 2.2 5B Video Generation</b>", html)

    def test_hardware_guide_mentions_vram_limit(self):
        guide = (ROOT / "docs" / "HARDWARE.md").read_text(encoding="utf-8")
        self.assertIn("4 GB", guide)
        self.assertIn("LivePortrait", guide)


if __name__ == "__main__":
    unittest.main()
