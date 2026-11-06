class RulesetRegistry:
    def __init__(self):
        self.rulesets={}

    def register(self,data):
        self.rulesets[data["id"]]=data

    def get(self,ruleset_id):
        return self.rulesets.get(ruleset_id)

    def active_rulesets(self):
        return list(self.rulesets.keys())
