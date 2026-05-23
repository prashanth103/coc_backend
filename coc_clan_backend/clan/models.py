from django.db import models

class Member(models.Model):

    ROLE_CHOICES = [
        ('leader', 'Leader'),
        ('coLeader', 'Co-Leader'),
        ('admin', 'Elder'),
        ('member', 'Member'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('warning', 'Warning'),
        ('inactive', 'Inactive'),
    ]

    tag = models.CharField(max_length=30, unique=True)

    name = models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    town_hall = models.IntegerField(default=1)

    trophies = models.IntegerField(default=0)

    donations = models.IntegerField(default=0)

    donations_received = models.IntegerField(default=0)

    clan_rank = models.IntegerField(default=0)

    exp_level = models.IntegerField(default=0)

    league_name = models.CharField(
        max_length=100,
        blank=True
    )

    league_icon = models.URLField(blank=True)

    # YOUR custom fields
    missed_wars = models.IntegerField(default=0)

    warning_level = models.CharField(
        max_length=20,
        default='low'
    )

    eligible_for_cwl = models.BooleanField(default=True)

    leader_notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    in_clan = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class War(models.Model):
    WAR_TYPES = [
        ('normal', 'Normal'),
        ('cwl', 'CWL'),
    ]

    WAR_STATES = [
        ('preparation', 'Preparation'),
        ('in_battle', 'In Battle'),
        ('war_ended', 'War Ended'),
    ]

    RESULT_TYPES = [
        ('win', 'Win'),
        ('loss', 'Loss'),
        ('draw', 'Draw'),
        ('pending', 'Pending'),
    ]

    war_type = models.CharField(max_length=20, choices=WAR_TYPES)

    enemy = models.CharField(max_length=100)
    enemy_badge = models.CharField(max_length=20, unique=True)
    enemy_level = models.IntegerField(default=1)

    size = models.IntegerField()

    state = models.CharField(max_length=20, choices=WAR_STATES)

    our_stars = models.IntegerField(default=0)
    enemy_stars = models.IntegerField(default=0)

    our_destruction = models.FloatField(default=0)
    enemy_destruction = models.FloatField(default=0)

    attacks_used = models.IntegerField(default=0)
    attacks_total = models.IntegerField(default=0)

    attacks_per_player = models.IntegerField(default=2)

    result = models.CharField(
        max_length=20,
        choices=RESULT_TYPES,
        default='pending'
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.war_type} vs {self.enemy}"

class Attack(models.Model):

    STAR_CHOICES = [
        (0, '0 Star'),
        (1, '1 Star'),
        (2, '2 Star'),
        (3, '3 Star'),
    ]

    war = models.ForeignKey(
        War,
        on_delete=models.CASCADE,
        related_name='attacks'
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='attacks'
    )

    target_base = models.IntegerField()

    stars = models.IntegerField(choices=STAR_CHOICES)

    destruction_percentage = models.FloatField(default=0)

    attack_used = models.BooleanField(default=True)

    attack_number = models.IntegerField(default=1)

    war_type = models.CharField(max_length=20)

    attack_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.stars}⭐"

class Notice(models.Model):

    NOTICE_TYPES = [
        ('mail', 'Clan Mail'),
        ('recruitment', 'Recruitment'),
        ('war', 'War Reminder'),
        ('cwl', 'CWL'),
        ('promotion', 'Promotion'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)

    message = models.TextField()

    notice_type = models.CharField(
        max_length=30,
        choices=NOTICE_TYPES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        