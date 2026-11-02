from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ProjectFilesTest(unittest.TestCase):
    def test_required_files_exist(self):
        for path in ("index.html", "run_server.py", "README.md", "start-animotion.bat"):
            self.assertTrue((ROOT / path).is_file(), path)

    def test_ai_scene_pipeline_available(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="screen-prompt"', html)
        self.assertIn('id="aiPrompt"', html)
        self.assertIn('id="aiCharacter"', html)
        self.assertIn('id="aiStyle"', html)
        self.assertIn("function createAiShotPlan()", html)
        self.assertIn("function buildShotPrompt(", html)
        self.assertIn("Sгенерировать все планы".replace("S", "С"), html)
        self.assertIn("videos", html)
        self.assertIn("same character", html.lower())
        self.assertIn('id="workflowFile"', html)
        self.assertIn('id="positiveNode"', html)

    def test_procedural_demo_is_separate_and_labelled(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="screen-demo"', html)
        self.assertIn('id="promptCanvas"', html)
        self.assertIn("promptMake", html)
        self.assertIn("НЕ AI-видео", html)
        self.assertIn("процедур", html.lower())

    def test_motion_lab_available(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="screen-motion"', html)
        self.assertIn('id="motionCanvas"', html)
        self.assertIn("MediaRecorder", html)
        self.assertIn("captureStream", html)
        self.assertIn("animotion-youtube-video.webm", html)

    def test_low_vram_guidance_present(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        guide = (ROOT / "docs" / "HARDWARE.md").read_text(encoding="utf-8")
        self.assertIn("RTX 2050", html)
        self.assertIn("4 GB", guide)
        self.assertIn("32 GB", guide)
        self.assertIn("16 GB", guide)
        self.assertIn("not general text-to-video", guide.lower())

    def test_readme_explains_how_to_open_and_limits(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Download ZIP", readme)
        self.assertIn("start-animotion.bat", readme)
        self.assertIn("публичный", readme.lower())
        self.assertIn("не обещает бесплатное неограниченное text-to-video", readme.lower())


if __name__ == "__main__":
    unittest.main()
