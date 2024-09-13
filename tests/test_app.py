import unittest
import streamlit as st
from streamlit.script_run_context import get_script_run_ctx

class TestApp(unittest.TestCase):
    def test_app_runs(self):
        ctx = get_script_run_ctx()
        self.assertIsNotNone(ctx, "Streamlit app failed to run in the test context")

    # You can extend this test by adding logic to check UI elements or mock user inputs

if __name__ == "__main__":
    unittest.main()

