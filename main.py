import boto3

# Cria o serviço com as suas credenciais da AWS #
client = boto3.client(
    service_name="sns",
    region_name='us-west-2',
    aws_access_key_id='KEY',
    aws_secret_access_key='KEY+9NIQ/EnsC0CaI1/LfHA9+EWD0'
)

# Envia o SMS para o número desejado #
client.publish(
    PhoneNumber="+551199999999",
    Message="Teste SMS AWS"
)