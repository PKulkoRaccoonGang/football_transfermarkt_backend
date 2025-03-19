import os
import google.generativeai as genai
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)


@api_view(["POST"])
def chat_with_gemini(request):
    user_message = request.data.get("message", "")

    if not user_message:
        return Response(
            {"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_message)

        return Response({"reply": response.text})

    except Exception as e:
        return Response(
            {"error": f"Server error: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
