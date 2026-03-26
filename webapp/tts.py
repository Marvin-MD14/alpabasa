from google.cloud import texttospeech
from django.http import HttpResponse, JsonResponse

def speak(request):
    text = request.GET.get("text")

    if not text:
        return JsonResponse({"error": "No text provided"}, status=400)

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="fil-PH",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0.85
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    return HttpResponse(response.audio_content, content_type="audio/mpeg")