#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import json
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

class TestArtifacts(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(__file__).parent / 'test_artifacts'
        self.test_dir.mkdir(exist_ok=True)

    def tearDown(self):
        for file in self.test_dir.glob('*'):
            file.unlink()
        self.test_dir.rmdir()

    def test_artifact_creation(self):
        artifact_path = self.test_dir / 'test_artifact.txt'
        artifact_path.write_text('This is a test artifact.')
        self.assertTrue(artifact_path.exists())

    def test_artifact_deletion(self):
        artifact_path = self.test_dir / 'test_artifact_to_delete.txt'
        artifact_path.write_text('This artifact will be deleted.')
        artifact_path.unlink()
        self.assertFalse(artifact_path.exists())

if __name__ == '__main__':
    unittest.main()
