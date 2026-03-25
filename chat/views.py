from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re

@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_msg = data.get('message', '').lower()
            
            # Enhanced conversational logic for Rentora
            reply = "I'm not sure I understand. Try asking about 'Apartments in Hyderabad', 'Private Rooms', or 'How to list a property'."
            
            if any(word in user_msg for word in ['hi', 'hello', 'hey', 'greetings']):
                reply = "Hello! 👋 I'm your Rentora assistant. I can help you find properties, explain our room types, or guide you on how to list your own place. What's on your mind?"
            
            elif any(word in user_msg for word in ['who are you', 'what are you', 'help']):
                reply = "I'm the Rentora AI Assistant! 🏠 I can help you search for Apartments, Villas, or PG rooms. I can also explain how to use our platform as a Tenant or Owner."

            elif 'apartment' in user_msg or 'flat' in user_msg:
                reply = "We have many Apartments and Studio Apartments available! 🏢 You can filter by 'Apartment' in the search results or type 'Apartment' in the search bar."

            elif 'villa' in user_msg:
                reply = "Looking for luxury? 🏰 We have standalone Villas and Entire Villa room options. Try searching for 'Villa' to see our premium listings."

            elif 'private' in user_msg or 'personal' in user_msg or 'single' in user_msg:
                reply = "If you want privacy, look for 'Private Room' listings. 🛌 These are perfect for individuals who want their own space."

            elif 'sharing' in user_msg or 'shared' in user_msg or 'pg' in user_msg:
                reply = "On a budget? 🤝 We have 'Shared Room' and 'PG / Room' options which are very cost-effective."

            elif 'cheap' in user_msg or 'budget' in user_msg or 'under' in user_msg:
                reply = "Rentora makes budget searching easy! 💰 Just type things like 'under 8000' or 'budget 15000' in the search bar at the top."

            elif any(word in user_msg for word in ['owner', 'list', 'add', 'sell', 'publish']):
                reply = "To list your property: \n1. Login as an **Owner** \n2. Go to your **Dashboard** \n3. Click **'Add Property'** \nIt's that simple! ✨"

            elif 'review' in user_msg or 'feedback' in user_msg:
                reply = "Only Tenants can leave reviews, but everyone can read them! ⭐️ Check the bottom of any property page to see what others are saying."

            elif 'wishlist' in user_msg or 'save' in user_msg:
                reply = "Found something you like? ❤️ Click 'Add to Wishlist' on the property page to save it for later!"

            elif any(word in user_msg for word in ['thanks', 'thank you', 'ok', 'great']):
                reply = "You're very welcome! 😊 Let me know if you need anything else to find your perfect home."

            elif any(word in user_msg for word in ['bye', 'goodbye']):
                reply = "Goodbye! Hope you find your dream home on Rentora! 👋"
                
            return JsonResponse({'reply': reply})
        except Exception as e:
            return JsonResponse({'reply': 'Sorry, something went wrong on my end.'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
