from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):
    LOW_BUDGET_CAMPAIGN = 2500.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, required_engagement)
        self.budget = LowBudgetCampaign.LOW_BUDGET_CAMPAIGN

    def check_eligibility(self, engagement_rate: float) -> bool:
        if engagement_rate >= (self.required_engagement * 0.9):
            return True

        return False

    def campaign_budget(self):
        return self.budget
