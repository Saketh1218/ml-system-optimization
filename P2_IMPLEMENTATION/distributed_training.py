class DistributedTrainingOrchestrator:
    """
    A class to orchestrate distributed training using both mirrored and multi-worker strategies.
    """

    def __init__(self, strategy='mirrored'):
        self.strategy = strategy

    def start_training(self):
        if self.strategy == 'mirrored':
            self.run_mirrored_strategy()
        elif self.strategy == 'multi-worker':
            self.run_multi_worker_strategy()
        else:
            raise ValueError("Unsupported strategy. Use 'mirrored' or 'multi-worker'.")

    def run_mirrored_strategy(self):
        """
        Implement the mirrored strategy training logic here.
        """
        print('Running training with mirrored strategy...')

    def run_multi_worker_strategy(self):
        """
        Implement the multi-worker strategy training logic here.
        """
        print('Running training with multi-worker strategy...')

# Example usage
if __name__ == '__main__':
    orchestrator = DistributedTrainingOrchestrator(strategy='mirrored')
    orchestrator.start_training()