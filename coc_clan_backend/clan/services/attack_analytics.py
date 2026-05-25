from clan.models import Attack, War


def build_attack_summary(war):

    attacks = Attack.objects.filter(
        war=war
    ).select_related(
        'attacker'
    ).order_by('attack_order')

    grouped_data = {}

    attacks_allowed = war.attacks_per_player

    enemy_map = {}

    current_war_data = getattr(
        war,
        'raw_data',
        {}
    )

    opponent_members = current_war_data.get(
        'opponent',
        {}
    ).get(
        'members',
        []
    )

    for enemy in opponent_members:

        enemy_map[enemy.get('tag')] = {
            'name': enemy.get('name'),
            'town_hall': enemy.get('townhallLevel')
        }

    for attack in attacks:

        attacker_id = attack.attacker.id

        if attacker_id not in grouped_data:

            grouped_data[attacker_id] = {
                'member_id': attack.attacker.id,
                'member': attack.attacker.name,
                'town_hall': attack.attacker.town_hall,
                'attacks_allowed': attacks_allowed,
                'attacks_used': 0,
                'missed_attacks': 0,
                'total_stars': 0,
                'avg_destruction': 0,
                'status': 'good',
                'attacks': []
            }

        enemy_data = enemy_map.get(
            attack.defender_tag,
            {}
        )

        grouped_data[attacker_id]['attacks'].append({
            'defender_tag': attack.defender_tag,
            'defender_name': enemy_data.get(
                'name',
                'Unknown'
            ),
            'defender_town_hall': enemy_data.get(
                'town_hall',
                0
            ),
            'stars': attack.stars,
            'destruction_percentage': attack.destruction_percentage,
            'duration': attack.duration
        })

        grouped_data[attacker_id]['attacks_used'] += 1

        grouped_data[attacker_id]['total_stars'] += attack.stars

    for member_data in grouped_data.values():

        attacks_used = member_data['attacks_used']

        member_data['missed_attacks'] = (
            attacks_allowed - attacks_used
        )

        total_destruction = sum(
            atk['destruction_percentage']
            for atk in member_data['attacks']
        )

        if attacks_used > 0:

            member_data['avg_destruction'] = round(
                total_destruction / attacks_used,
                2
            )

        if member_data['missed_attacks'] == attacks_allowed:

            member_data['status'] = 'missed'

        elif member_data['missed_attacks'] > 0:

            member_data['status'] = 'warning'

    return list(grouped_data.values())