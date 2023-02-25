class Config:
    # Telegram API Key
    API_KEY = 'your_api_key_here'

    # Admin ID (your Telegram user ID)
    ADMIN = your_admin_id_here

    # Donation button data
    DONATION_DATA = {
        'title': 'Donate',
        'description': 'Support our group!',
        'payload': 'donation'
    }

    # Plan button data
    PLAN_DATA = {
        'title': 'Plans',
        'description': 'View our membership plans',
        'payload': 'plans'
    }

    # Group button data
    GROUP_DATA = {
        'title': 'Group',
        'description': 'Join our group',
        'url': 'https://t.me/your_group_name_here'
    }

    # Channel button data
    CHANNEL_DATA = {
        'title': 'Channel',
        'description': 'Join our channel',
        'url': 'https://t.me/your_channel_name_here'
    }

    # Donation plan data (replace with your own plans)
    PLAN_1_DATA = {
        'title': 'Bronze',
        'description': 'Access to exclusive content',
        'price': 5,
        'payload': 'bronze'
    }

    PLAN_2_DATA = {
        'title': 'Silver',
        'description': 'Access to exclusive content and giveaways',
        'price': 10,
        'payload': 'silver'
    }

    PLAN_3_DATA = {
        'title': 'Gold',
        'description': 'Access to exclusive content, giveaways, and early access to events',
        'price': 20,
        'payload': 'gold'
    }

    # Broadcast message limit (change as needed)
    BROADCAST_LIMIT = 10
