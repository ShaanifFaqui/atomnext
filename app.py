from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Knowledge base for the chatbot
KNOWLEDGE_BASE = {
    'greetings': [
        'hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'
    ],
    'company': [
        'atom next', 'atom next solutions', 'atom next ai', 'about atom', 'who are you',
        'company', 'about company', 'about us', 'tell me about atom'
    ],
    'services': {
        'web_development': [
            'web development', 'website', 'web app', 'web application', 'website development',
            'frontend', 'backend', 'full stack', 'responsive design'
        ],
        'mobile_apps': [
            'mobile app', 'mobile application', 'ios', 'android', 'app development',
            'cross platform', 'react native', 'flutter'
        ],
        'ai_solutions': [
            'ai', 'artificial intelligence', 'machine learning', 'ml', 'chatbot',
            'automation', 'data analytics', 'predictive analytics'
        ],
        'custom_software': [
            'custom software', 'software development', 'enterprise software',
            'business software', 'custom solution'
        ]
    },
    'pricing': [
        'price', 'cost', 'pricing', 'how much', 'budget', 'quote', 'estimate'
    ],
    'contact': [
        'contact', 'reach', 'get in touch', 'email', 'phone', 'address',
        'location', 'office', 'meet'
    ],
    'process': [
        'process', 'how it works', 'workflow', 'timeline', 'duration',
        'steps', 'methodology', 'approach'
    ]
}

# Responses for different categories
RESPONSES = {
    'greeting': [
        "Hello! 👋 I'm Atom Next AI's assistant. How can I help you today?",
        "Hi there! 👋 Welcome to Atom Next AI. What can I do for you?",
        "Hey! 👋 I'm here to help you with any questions about our services."
    ],
    'company': [
        """Atom Next Solutions is a cutting-edge technology company founded by Nasheel Damudi, Shaanif Ahmed, and Azhar Ali. We specialize in transforming businesses through innovative technology solutions.

Our expertise includes:
• Web Development
• Mobile App Development
• AI Solutions
• Custom Software Development

We're passionate about helping businesses grow through technology and innovation. Our team combines technical expertise with creative problem-solving to deliver exceptional results.""",
        
        """Welcome to Atom Next Solutions! We're a dynamic team of technology experts dedicated to helping businesses succeed in the digital age.

Founded by industry professionals, we offer:
• Modern Web Solutions
• Mobile Applications
• AI Integration
• Custom Software

Our mission is to empower businesses with technology that drives growth and innovation."""
    ],
    'web_development': [
        "We offer comprehensive web development services including responsive websites, web applications, and e-commerce solutions. Our team uses modern technologies like React, Angular, and Node.js to create robust and scalable web solutions.",
        "Our web development services cover everything from simple websites to complex web applications. We focus on creating user-friendly, responsive, and high-performance solutions tailored to your needs."
    ],
    'mobile_apps': [
        "We develop both native and cross-platform mobile applications for iOS and Android. Our mobile solutions are designed to provide excellent user experience and performance across all devices.",
        "Our mobile app development services include iOS, Android, and cross-platform development using technologies like React Native and Flutter. We ensure your app is fast, secure, and user-friendly."
    ],
    'ai_solutions': [
        "We provide cutting-edge AI solutions including chatbots, process automation, and data analytics. Our AI services help businesses streamline operations and make data-driven decisions.",
        "Our AI solutions range from intelligent chatbots to complex machine learning systems. We help businesses leverage artificial intelligence to improve efficiency and gain competitive advantages."
    ],
    'custom_software': [
        "We develop custom software solutions tailored to your specific business needs. Our team creates scalable and maintainable software that helps streamline your operations.",
        "Our custom software development services focus on creating solutions that perfectly match your business requirements. We ensure high quality, security, and scalability in every project."
    ],
    'pricing': [
        "Our pricing varies based on project requirements and scope. Would you like to schedule a consultation to discuss your specific needs and get a detailed quote?",
        "We provide customized quotes based on your project requirements. Let's schedule a call to understand your needs better and provide an accurate estimate."
    ],
    'contact': [
        "You can reach us through our contact form on the website or schedule a consultation call. Would you like me to help you with that?",
        "We're available through multiple channels. You can contact us via the website, email, or schedule a call. I can help you with any of these options."
    ],
    'process': [
        "Our development process includes: 1) Discovery and consultation, 2) Planning and design, 3) Development, 4) Testing, 5) Deployment, and 6) Ongoing support. Would you like to know more about any specific phase?",
        "We follow a systematic approach: starting with understanding your requirements, creating a detailed plan, developing the solution, thorough testing, and providing ongoing support. Each phase is designed to ensure the best results."
    ],
    'fallback': [
        "I'm not sure I understand. Could you please rephrase your question? I can help you with information about our services, pricing, or process.",
        "I'm still learning! Could you try asking that in a different way? I can tell you about our web development, mobile apps, AI solutions, or custom software services."
    ]
}

def get_response(message):
    message = message.lower()
    
    # Check for greetings
    if any(greeting in message for greeting in KNOWLEDGE_BASE['greetings']):
        return {'response': random.choice(RESPONSES['greeting']), 'status': 'success'}
    
    # Check for company information
    if any(term in message for term in KNOWLEDGE_BASE['company']):
        return {'response': random.choice(RESPONSES['company']), 'status': 'success'}
    
    # Check for services
    for service, keywords in KNOWLEDGE_BASE['services'].items():
        if any(keyword in message for keyword in keywords):
            return {'response': random.choice(RESPONSES[service]), 'status': 'success'}
    
    # Check for pricing
    if any(term in message for term in KNOWLEDGE_BASE['pricing']):
        return {'response': random.choice(RESPONSES['pricing']), 'status': 'success'}
    
    # Check for contact
    if any(term in message for term in KNOWLEDGE_BASE['contact']):
        return {'response': random.choice(RESPONSES['contact']), 'status': 'success'}
    
    # Check for process
    if any(term in message for term in KNOWLEDGE_BASE['process']):
        return {'response': random.choice(RESPONSES['process']), 'status': 'success'}
    
    # Fallback response
    return {'response': random.choice(RESPONSES['fallback']), 'status': 'success'}

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({
                'response': 'Please provide a message.',
                'status': 'error'
            }), 400
        
        response = get_response(user_message)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'response': 'I apologize, but I encountered an error. Please try again.',
            'status': 'error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 