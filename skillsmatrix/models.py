from django.db import models
from django.contrib.auth.models import User

# Account Tiers Options
ACCOUNT_TIERS = [
    ('free', 'Free Tier'),
    ('startup', 'Startup Tier'),
    ('growth', 'Growth Tier'),
    ('business', 'Business Tier'),
    ('enterprise', 'Enterprise Tier'),
]

# Pre-built Skills Table
class PreBuiltSkill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    source = models.CharField(max_length=255)
    external_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Custom Skills Table
class CustomSkill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    weblink = models.URLField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Teams Table
class Team(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_teams')
    team_admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_teams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Team Members Table
class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_team_admin = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} in {self.team.name}"

# Skills Table
class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Skill Requirements Table
class SkillRequirement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    required_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.skill.name} for {self.team.name}"

# User Skills Table
class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)
    pre_built_skill = models.ForeignKey(PreBuiltSkill, on_delete=models.CASCADE, null=True, blank=True)
    self_evaluation_level = models.IntegerField()
    attachment_file_path = models.CharField(max_length=255, null=True, blank=True)
    attachment_file_type = models.CharField(max_length=50, null=True, blank=True)
    attachment_upload_date = models.DateTimeField(null=True, blank=True)
    user_notes = models.TextField(null=True, blank=True)
    admin_feedback = models.TextField(null=True, blank=True)
    verification_status = models.CharField(max_length=50, null=True, blank=True)
    skill_review_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s skill"

# Extended User Model for Account Tiers
class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_tier = models.CharField(max_length=20, choices=ACCOUNT_TIERS)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
