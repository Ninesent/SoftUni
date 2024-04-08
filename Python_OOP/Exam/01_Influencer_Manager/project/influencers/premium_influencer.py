from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENT = 0.85
    CAMPAIGN_MAPPER = {
        "HighBudgetCampaign": 1.5,
        "LowBudgetCampaign": 0.8,
    }

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return float(campaign.campaign_budget() * PremiumInfluencer.INITIAL_PAYMENT_PERCENT)

    def reached_followers(self, campaign_type: str) -> int:
        return int((self.followers * self.engagement_rate) * PremiumInfluencer.CAMPAIGN_MAPPER[campaign_type])
