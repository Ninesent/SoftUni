from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    HIGH_CAMPAIGN_BUDGET = 5000.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, required_engagement)
        self.budget = HighBudgetCampaign.HIGH_CAMPAIGN_BUDGET

    def check_eligibility(self, engagement_rate: float) -> bool:
        if engagement_rate >= (self.required_engagement * 1.20):
            return True

        return False

    def campaign_budget(self):
        return self.budget
