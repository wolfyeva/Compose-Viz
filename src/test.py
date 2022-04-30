class TestYaml(YamaleTestCase):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    schema = 'schema.yaml'
    yaml = 'docker-compose.yaml'
    # or yaml = ['data-*.yaml', 'some_data.yaml']

    def runTest(self):
        self.assertTrue(self.validate())