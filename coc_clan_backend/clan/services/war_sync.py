from clan.models import War
from datetime import datetime
from django.utils.timezone import make_aware


def parse_coc_time(time_str):

    dt = datetime.strptime(
        time_str,
        "%Y%m%dT%H%M%S.000Z"
    )

    return make_aware(dt)


def calculate_war_result(
    our_stars,
    enemy_stars,
    our_destruction,
    enemy_destruction
):

    if our_stars > enemy_stars:
        return 'win'

    elif our_stars < enemy_stars:
        return 'loss'

    else:

        if our_destruction > enemy_destruction:
            return 'win'

        elif our_destruction < enemy_destruction:
            return 'loss'

        else:
            return 'draw'


def sync_current_war(data):

    clan = data.get('clan', {})
    opponent = data.get('opponent', {})

    war_state = data.get('state', '')

    our_stars = clan.get('stars', 0)

    enemy_stars = opponent.get('stars', 0)

    our_destruction = clan.get(
        'destructionPercentage',
        0
    )

    enemy_destruction = opponent.get(
        'destructionPercentage',
        0
    )

    if war_state == 'warEnded':

        result = calculate_war_result(
            our_stars,
            enemy_stars,
            our_destruction,
            enemy_destruction
        )
    else:
        result = 'pending'


    war, created = War.objects.update_or_create(
        start_time=parse_coc_time(
            data['startTime']
        ),
        defaults={
            'war_type': 'normal',
            'enemy': opponent.get('name', ''),
            'enemy_badge': opponent.get('badgeUrls', {}).get('medium', ''),
            'enemy_level': opponent.get('clanLevel', 1),
            'size': data.get('teamSize', 0),
            'state': data.get('state', ''),
            'our_stars': clan.get('stars', 0),
            'enemy_stars': opponent.get('stars', 0),
            'our_destruction': clan.get('destructionPercentage', 0),
            'enemy_destruction': opponent.get('destructionPercentage', 0),
            'attacks_used': clan.get('attacks', 0),
            'attacks_total': data.get('teamSize', 0) * data.get('attacksPerMember', 0),
            'attacks_per_player': data.get('attacksPerMember', 2),
            'result': result,
            'end_time': parse_coc_time(
                data['endTime']
            ),
        }
    )

    return war