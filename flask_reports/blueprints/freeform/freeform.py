from datetime import timedelta
from typing import Annotated, List, Optional
from flask import Blueprint, url_for, render_template, redirect, request, session
from pydantic import BaseModel, BeforeValidator
from openai import OpenAI, AsyncOpenAI
from flask_reports.models.web import Response
from flask_wtf import FlaskForm
from wtforms import HiddenField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List
from pydantic import BaseModel
from wtforms.csrf.session import SessionCSRF
import instructor
from instructor import llm_validator

freeform_bp = Blueprint('freeform', __name__, template_folder="ff_templates")

class FreeformForm(FlaskForm):
    class Meta:
        csrf = False 
        csrf_class = SessionCSRF  
        csrf_secret = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
        csrf_time_limit = timedelta(minutes=20)
    name = StringField('name', validators=[DataRequired()])
    context = SelectField(u'context', choices=[('cooking', 'Cooking'), ('health', 'Health'), ('code_help', 'Code Help')])
    prompt = TextAreaField('prompt')

class GeneralResponse(BaseModel):
    context_relevancy_score: int
    response: str

@freeform_bp.route("/form", methods=['GET'])
def writer_form() -> FreeformForm:
    form = FreeformForm()
    return render_template("freeform.html", form=form)

@freeform_bp.route('/submit', methods=['POST'])
def submit():
    form = FreeformForm(meta={'csrf_context': session})
    print(form.validate())
    print(form.validate_on_submit())
    print(form.errors)
    if form.validate_on_submit():
    # form = WriterForm(request.POST)
    # if request.method == 'POST' and form.validate():
        # enables `response_model` in create call

        context = f"""Please limit your responses to only pertain to the following: {request.form['context']}"""
        question = f"""{request.form['prompt']}"""

        client = instructor.patch(
            OpenAI(
                base_url="http://localhost:11434/v1",
                api_key="ollama",  # required, but unused
            ),
            mode=instructor.Mode.JSON,
        )
        print(request.form['prompt'])
        resp = client.chat.completions.create(
            # Gemma does not work
            model="codellama",
            max_retries=5,
            messages=[
                {
                    "role": "system",
                    "content": "You are a system that answers questions based on the context. Answer exactly what the question asks using the context.",
                },
                {
                    "role": "user",
                    "content": f"""using the context: {context}\n\nAnswer the following question or respond to the following prompt: {question}. 
                                Afterwards, please provide a context_relevancy_score from 1 to 10 that rates the relevancy of the prompt entered and the context provided."""
                },
            ],
            response_model=GeneralResponse,
        )
        print(resp)
        print(resp.response)
        # return redirect('/success')
        return render_template('ff_result.html', resp=resp)
    return render_template('ff_result.html', resp=None)