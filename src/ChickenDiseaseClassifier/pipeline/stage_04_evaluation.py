from ChickenDiseaseClassifier.config.configuration import ConfigurationManager
from ChickenDiseaseClassifier.components.model_evaluation import Evaluation
from ChickenDiseaseClassifier import logger




STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()