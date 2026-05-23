from clan.models import Member


def sync_members(clan_members):

    current_tags = []

    for player in clan_members:

        current_tags.append(player['tag'])

        Member.objects.update_or_create(
            tag=player['tag'],
            defaults={
                'name': player['name'],
                'role': player['role'],
                'town_hall': player['townHallLevel'],
                'trophies': player['trophies'],
                'donations': player['donations'],
                'donations_received': player['donationsReceived'],
                'clan_rank': player['clanRank'],
                'exp_level': player['expLevel'],
                'league_name': player.get('league', {}).get('name', ''),
                'league_icon': player.get('league', {})
                    .get('iconUrls', {})
                    .get('small', ''),
                'in_clan': True
            }
        )

    Member.objects.exclude(
        tag__in=current_tags
    ).update(in_clan=False)