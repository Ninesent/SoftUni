from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENT = 0.45
    CAMPAIGN_MAPPER = {
        "HighBudgetCampaign": 1.2,
        "LowBudgetCampaign": 0.9,
    }

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        return float(campaign.campaign_budget() * StandardInfluencer.INITIAL_PAYMENT_PERCENT)

    def reached_followers(self, campaign_type: str) -> int:
        return int((self.followers * self.engagement_rate) * StandardInfluencer.CAMPAIGN_MAPPER[campaign_type])
