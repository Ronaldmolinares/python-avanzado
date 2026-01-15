"""Tests for analyzer."""

import unittest
from unittest.mock import Mock, patch

from platzi_news.analysis.analyzer import GeminiAnalyzer, get_analyzer
from platzi_news.core.exceptions import AnalysisError
from platzi_news.core.models import Article


class TestGeminiAnalyzer(unittest.TestCase):
    """Test GeminiAnalyzer."""

    @patch("platzi_news.analysis.analyzer.genai.Client")
    def test_analyze_success(self, mock_client_class):
        mock_client = Mock()
        mock_client_class.return_value = mock_client
        mock_response = Mock()
        mock_response.text = "Test answer"
        mock_client.models.generate_content.return_value = mock_response

        analyzer = GeminiAnalyzer("fake_key")
        articles = [Article("Test", "Desc", "http://example.com")]
        answer = analyzer.analyze(articles, "What is this about?")
        self.assertEqual(answer, "Test answer")

    @patch("platzi_news.analysis.analyzer.genai.Client")
    def test_analyze_no_articles(self, mock_client_class):
        analyzer = GeminiAnalyzer("fake_key")
        answer = analyzer.analyze([], "Question")
        self.assertEqual(answer, "No se encontraron artículos para analizar.")

    @patch("platzi_news.analysis.analyzer.genai.Client")
    def test_analyze_error(self, mock_client_class):
        mock_client = Mock()
        mock_client_class.return_value = mock_client
        mock_client.models.generate_content.side_effect = Exception("API error")

        analyzer = GeminiAnalyzer("fake_key")
        articles = [Article("Test", "Desc", "http://example.com")]
        with self.assertRaises(AnalysisError):
            analyzer.analyze(articles, "Question")


class TestGetAnalyzer(unittest.TestCase):
    """Test get_analyzer factory."""

    @patch("platzi_news.config.settings")
    def test_get_analyzer_success(self, mock_settings):
        mock_settings.google_api_key = "fake_key"
        analyzer = get_analyzer()
        self.assertIsInstance(analyzer, GeminiAnalyzer)


if __name__ == "__main__":
    unittest.main()
