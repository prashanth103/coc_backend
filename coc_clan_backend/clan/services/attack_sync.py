from clan.models import Attack, Member


def sync_attacks(war, data):

    clan_members = data.get('clan', {}).get('members', [])

    for member_data in clan_members:

        attacker_tag = member_data.get('tag')

        try:
            attacker = Member.objects.get(tag=attacker_tag)
        except Member.DoesNotExist:
            continue

        attacks = member_data.get('attacks', [])

        for atk in attacks:

            Attack.objects.update_or_create(
                war=war,
                attacker=attacker,
                attack_order=atk.get('order', 0),
                defaults={
                    'defender_tag': atk.get('defenderTag', ''),
                    'stars': atk.get('stars', 0),
                    'destruction_percentage': atk.get('destructionPercentage', 0),
                    'duration': atk.get('duration', 0),
                }
            )