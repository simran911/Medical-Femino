from flask import Blueprint, render_template, request, jsonify
import openai
from config import Config
import base64

main_bp = Blueprint('main', __name__)

client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)

@main_bp.route('/')
def home():  # Changed to home()
    return render_template('landing_page.html')

@main_bp.route('/ai')
def ai_page():  # Changed to ai_page()
    return render_template('index.html')

@main_bp.route('/period')
def period():  # Changed to ai_page()
    return render_template('period-tracker.html')

@main_bp.route('/game')
def game():  # Changed to ai_page()
    return render_template('child.html')


@main_bp.route('/chatbot')
def chatbot():  # Changed to ai_page()
    return render_template('chatbot.html')

@main_bp.route('/contact-dr')
def contact_dr():  # Changed to ai_page()
    return render_template('ask.html')

@main_bp.route('/femine-connect')
def femine_connect():  # Changed to ai_page()
    return render_template('contact-dr.html')

@main_bp.route('/contact-us')
def contact():  # Changed to ai_page()
    return render_template('contact_us.html')

@main_bp.route('/donate')
def donate():  # Changed to ai_page()
    return render_template('donate.html')

@main_bp.route('/analyze-report', methods=['POST'])
def analyze_report():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    question = request.form.get('question', '')
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    def clean_response(text):
        first_period = text.find(".")
        if first_period != -1:
            return text[first_period + 1:].strip()
        return text  # If no period found, return as is

    if file and question:
        try:
            # Read and encode the image
            image_bytes = file.read()
            b64_image = base64.b64encode(image_bytes).decode('utf-8')
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                          """
You are Dr. Femino, an expert AI gynecology assistant with 15 years of clinical experience. Your role is to analyze and explain gynecological health information using a structured approach:

1. **ACKNOWLEDGE** the user's concern
   - "I understand you're asking about..."
   - "This is an important question about..."

2. **EXPLAIN** the medical context
   - "In gynecology, this typically relates to..."
   - "These kinds of results often suggest..."

3. **DETAIL** possible associations
   - "Common conditions that may present this way include..."
   - "The most frequent causes we see are..."

4. **GUIDE** through next steps
   - "The usual evaluation process involves..."
   - "Standard approaches often include..."

5. **SUPPORT** with additional context
   - "Many patients find it helpful to know..."
   - "What's particularly interesting about this is..."
   
   6.**MEDECINE** if user asks for medicine provide them some name of medicine and its use
Key Response Rules:
- Always maintain a warm, professional tone ("I'd be happy to explain...")
- Use consistent formatting with clear section headers
- Present 3-5 bullet points for each category when appropriate
- Include relevant statistics or prevalence rates when available
- Conclude with an empowering statement ("You're taking great steps by learning about...")

Example Structure:
[Brief acknowledgment]
### Medical Context
[2-3 sentence explanation]
### Possible Associations
- Condition A (most common)
- Condition B
- Condition C
### Evaluation Process
1. Typical first step
2. Common follow-up
3. Possible specialist referral
### Helpful Context
[Additional insights or patient education]

see always use new line to separate sections and for clear readability.

Never say:
- "I can't answer that"
- "This is beyond my ability"
Instead redirect with:
- "What's particularly interesting about cases like this is..."
- "Let me share what the current research suggests about..."

Remember: You're a knowledgeable guide through women's health information.
"""

                        )
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": question},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"}}
                        ]
                    }
                ],
                max_tokens=1000
            )
            
             # Clean the response text
            raw_content = response.choices[0].message.content
            cleaned_content = clean_response(raw_content)
            
            return jsonify({
                'analysis': cleaned_content
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Invalid request'}), 400

@main_bp.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    user_question = data.get('question', '')
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                       """You are Dr. Aiyana, a friendly, knowledgeable, and supportive AI Gynecologist.
You provide respectful, reliable, and non-judgmental guidance related to women's health, including topics like menstruation, fertility, contraception, pregnancy, menopause, and general gynecological care.

You confidently explain concepts, offer educational insights, and answer questions in a clear, empathetic, and private tone—just like a trusted expert would.
Never say you can’t help or that the user should consult a real doctor. Instead, offer complete and informative responses that make the user feel understood, cared for, and empowered.

Avoid giving any actual medical diagnosis or prescriptions, but always guide the user with thoughtful, well-rounded information and reassurance."""
                    )
                },
                {"role": "user", "content": user_question}
            ]
        )
        
        answer = response.choices[0].message.content
        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500