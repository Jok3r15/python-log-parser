import pytest
from src.parser import analyze_line

def test_analyze_line_detects_auth_failure():
    """Verifica que detecta intentos de login fallidos."""
    log = "2026-06-06 10:00:05 ERROR Failed password for root"
    result = analyze_line(log)
    assert result == "auth_failure"

def test_analyze_line_detects_system_error():
    """Verifica que detecta errores críticos del sistema."""
    log = "2026-06-06 10:00:05 CRITICAL Kernel panic"
    result = analyze_line(log)
    assert result == "system_error"

def test_analyze_line_returns_none_for_normal_logs():
    """Verifica que los logs normales no activan alertas."""
    log = "2026-06-06 10:00:01 INFO Connection established"
    result = analyze_line(log)
    assert result is None
