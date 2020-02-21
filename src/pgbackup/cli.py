from argparse import ArgumentParser, Action

class DriverAction(Action):
    def __call__(self,parser,namespace,values,option_string='None'):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Back up PosrgreSQL database locally or to AWS S3
    """)

    parser.add_argument("url", help="url of the database to backup")
    parser.add_argument("--driver", '-d',
            help="how and where to store backup",
            nargs=2,
            metavar=("DRIVER","DESTINATION"),
            action=DriverAction,
            required=True)
    return parser

def main():
    import boto3
    import time
    from pgbackup import pgdump, storage
    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        # TODO: create a batter name based on the database name and date
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)
