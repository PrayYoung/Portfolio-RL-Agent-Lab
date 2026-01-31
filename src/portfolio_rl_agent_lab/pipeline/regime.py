from __future__ import annotations

from typing import Literal


RegimeSource = Literal["heuristic", "local", "student"]


def run_regime_pipeline(source: RegimeSource) -> None:
    if source == "heuristic":
        from portfolio_rl_agent_lab.llm.build_regime_features import main as m
        m()
    elif source == "local":
        from portfolio_rl_agent_lab.llm.build_regime_features_local import main as m
        m()
    elif source == "student":
        from portfolio_rl_agent_lab.student.build_regime_features_student import main as m
        m()
    else:
        raise ValueError(f"Unknown regime source: {source}")


if __name__ == "__main__":
    run_regime_pipeline("heuristic")
