from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectFilesTest(unittest.TestCase):
    def test_required_files_exist(self):
        for path in ("index.html", "run_server.py", "README.md", "start-animotion.bat"):
            self.assertTrue((ROOT / path).is_file(), path)

    def test_motion_lab_available(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="screen-motion"', html)
        self.assertIn('id="motionCanvas"', html)
        self.assertIn("MediaRecorder", html)
        self.assertIn("captureStream", html)
        self.assertIn("animotion-youtube-video.webm", html)

    def test_prompt_animator_available_without_images(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="screen-prompt"', html)
        self.assertIn('id="promptDescription"', html)
        self.assertIn("promptMake", html)
        self.assertIn("promptSpace", html)
        self.assertIn("promptCity", html)
        self.assertIn("promptOcean", html)
        self.assertIn("animotion-prompt-animation.webm", html)
        self.assertIn("procedural", html.lower())

    def test_low_vram_guidance_present(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        guide = (ROOT / "docs" / "HARDWARE.md").read_text(encoding="utf-8")
        self.assertIn("RTX 2050", html)
        self.assertIn("4 GB", guide)
        self.assertIn("LivePortrait", guide)
        self.assertNotIn("выбери <b>Wan 2.2 5B Video Generation</b>", html)

    def test_readme_explains_how_to_open(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Download ZIP", readme)
        self.assertIn("start-animotion.bat", readme)
        self.assertIn("Private", readme)
        self.assertIn("Prompt Animator", readme)


if __name__ == "__main__":
    unittest.main()
