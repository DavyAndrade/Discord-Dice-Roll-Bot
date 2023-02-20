import discord
from discord import app_commands
import random

id_do_servidor = ##### ID do Server Aqui

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) 
            self.synced = True
        print(f"Logado como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd4', description='Rola um dado de 4 lados')
async def slashd4(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D4", description=(
        random.randint(1, 4)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd6', description='Rola um dado de 6 lados')
async def slashd6(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D6", description=(
        random.randint(1, 6)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd8', description='Rola um dado de 8 lados')
async def slashd6(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D8", description=(
        random.randint(1, 8)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd10', description='Rola um dado de 10 lados')
async def slashd6(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D10", description=(
        random.randint(1, 10)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd12', description='Rola um dado de 12 lados')
async def slashd20(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D12", description=(
        random.randint(1, 12)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)


@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd20', description='Rola um dado de 20 lados')
async def slashd20(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D20", description=(
        random.randint(1, 20)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'd100', description='Rola um dado de 100 lados')
async def slashd20(interaction: discord.Interaction):
    embed = discord.Embed(title="Resultado do D100", description=(
        random.randint(1, 100)), color=(0xF85252))
    await interaction.response.send_message(embed=embed, ephemeral = False)

aclient.run('token do bot aqui')