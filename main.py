import gymnasium

env = gymnasium.make("ALE/Riverraid-v5", render_mode="human", obs_type="ram")
observation, info = env.reset(seed=42)

def convert(n):
  out = 0
  for bit in n:
    out = (out << 1) | bit
  return out

while True:
  acao = env.action_space.sample()

  ambiente, recompensa, finalizado, paralizado, info = env.step(acao)

  ambiente_txt = convert(ambiente)
  recompensa_txt = "Recompensa: [%s]" % recompensa
  fim_txt = "Finalizado: [%s]" % finalizado
  acao_txt = "Ação: [%s]" % acao

  if (recompensa < 0):
    recompensa_txt = recompensa_txt
  elif (recompensa > 0):
    recompensa_txt = recompensa_txt

  if (finalizado):
    fim_txt = fim_txt

  print(ambiente_txt, recompensa_txt, fim_txt, acao_txt)

  if finalizado or paralizado:
    break

env.close()