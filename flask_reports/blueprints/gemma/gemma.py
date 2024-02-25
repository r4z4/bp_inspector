from datetime import timedelta
from typing import Annotated, List
from flask import Blueprint, url_for, render_template, redirect, request, session
from pydantic import BaseModel, BeforeValidator
from openai import OpenAI, AsyncOpenAI
from flask_reports.models.web import Response
from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, TextAreaField
from wtforms.validators import DataRequired
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from pydantic import BaseModel
from wtforms.csrf.session import SessionCSRF
import instructor
from instructor import llm_validator

gemma_bp = Blueprint('gemma', __name__, template_folder="templates")

class FamousWriter(BaseModel):
    name: Annotated[
        str,
        BeforeValidator(
            llm_validator("do not answer 'Unknown Author'. If unknown, make an educated guess.", allow_override=True)
        ),
    ]
    style: str
    traits: List[str]

class WriterForm(FlaskForm):
    class Meta:
        csrf = False  # Enable CSRF
        csrf_class = SessionCSRF  # Set the CSRF implementation
        csrf_secret = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
        csrf_time_limit = timedelta(minutes=20)
        # Any other CSRF settings here.
    name = StringField('name', validators=[DataRequired()])
    content = TextAreaField('content')

@gemma_bp.route("/writer")
def writer() -> Response[FamousWriter]:
        mock_fw = FamousWriter(name="Greg Cote", style="Dry Humor", traits=["Loveable", "Humorous", "Nostalgic"])
        mock_bad = Response(data=None)
        mock_good = Response(data=mock_fw)
        return render_template("gemma.html", resp=mock_bad)


@gemma_bp.route("/writer/form", methods=['GET'])
def writer_form() -> WriterForm:
    form = WriterForm()
    return render_template("writer.html", form=form)

@gemma_bp.route('/writer/submit', methods=['POST'])
def submit():
    default_resp = FamousWriter(name="Blouse", style="Blousing It", traits=["Ugh","Huh"])
    form = WriterForm(meta={'csrf_context': session})
    print(form.validate())
    print(form.validate_on_submit())
    print(form.errors)
    if form.validate_on_submit():
    # form = WriterForm(request.POST)
    # if request.method == 'POST' and form.validate():
        # enables `response_model` in create call

        context = """I am trying to identify which famous author would have most likely written this bit of text, and get a response with their name, writing style and a list of descriptors for their work."""
                    # Do not answer "Unknown Author", if it is unknown, please just guess at which author could have written it."""
        question = f"""Judging based on syntax, use of prose and general style, can you tell me which famous author would have most likely written this: {request.form['content']}"""

        client = instructor.patch(
            OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama",  # required, but unused
            ),
            mode=instructor.Mode.JSON,
        )
        print(request.form['content'])
        resp = client.chat.completions.create(
            # Gemma does not work
            model="codellama",
            max_retries=2,
            messages=[
                {
                    "role": "system",
                    "content": "You are a system that answers questions based on the context. Answer exactly what the question asks using the context.",
                },
                {
                    "role": "user",
                    "content": f"using the context: {context}\n\nAnswer the following question: {question}",
                },
            ],
            response_model=FamousWriter,
        )
        print(resp)
        # return redirect('/success')
        return render_template('result.html', resp=resp)
    return render_template('result.html', resp=default_resp)