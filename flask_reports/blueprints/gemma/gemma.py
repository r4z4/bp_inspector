from typing import List
from flask import Blueprint, url_for, render_template, redirect
from pydantic import BaseModel
from openai import OpenAI, AsyncOpenAI
from flask_reports.models.web import Response

gemma_bp = Blueprint('gemma', __name__, template_folder="templates")

class FamousWriter(BaseModel):
    name: str
    style: str
    traits: List[str]

@gemma_bp.route("/writer")
def writer() -> Response[FamousWriter]:
        mock_fw = FamousWriter(name="Greg Cote", style="Dry Humor", traits=["Loveable", "Humorous", "Nostalgic"])
        mock_bad = Response(data=None)
        mock_good = Response(data=mock_fw)
        return render_template("gemma.html", resp=mock_bad)
