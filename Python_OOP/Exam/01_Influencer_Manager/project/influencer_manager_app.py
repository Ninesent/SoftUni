from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp():
    VALID_INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer,
    }

    VALID_CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign,
    }

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float) -> str:

        try:
            influencer = InfluencerManagerApp.VALID_INFLUENCER_TYPES[influencer_type](username, followers,
                                                                                      engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda i: i.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float) -> str:

        for c in self.campaigns:
            if c.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."

        try:
            campaign = InfluencerManagerApp.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        except KeyError:
            return f"{campaign_type} is not a valid campaign type."

        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."



    def participate_in_campaign(self, influencer_username: str, campaign_id: int) -> str:

        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        availability = campaign.check_eligibility(influencer.engagement_rate)

        if not availability:
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)

        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):

        total_reached_followers = {}

        campaigns = [c for c in self.campaigns if len(c.approved_influencers) > 0]

        for campaign in campaigns:
            total_reached_followers[campaign] = sum([i.reached_followers(campaign.__class__.__name__) for i in campaign.approved_influencers])

        return total_reached_followers

    def influencer_campaign_report(self, username: str):

        influencer = next(filter(lambda i: i.username == username, self.influencers))

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):

        valid_campaigns = filter(lambda c: len(c.approved_influencers) > 0, self.campaigns)

        campaigns = sorted(valid_campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))

        result = ""

        campaign_dict = self.calculate_total_reached_followers()

        for c in campaigns:

            result += (f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
                       f"Total budget: ${c.budget:.2f}, "
                       f"Total reached followers: {campaign_dict[c]}\n")

        return (f"$$ Campaign Statistics $$\n"
                f"{result}")
