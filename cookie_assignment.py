from thinkbayes import Pmf


class Cookie(Pmf):
    def __init__(self, hypos):
        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()

    def Update(self, data):
        print(f"Updating: {data}")
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    def UpdateAndRemove(self, data):
        print(f"Updating and Removing: {data}")
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()
        for hypo, prob in self.Items():
            self.mixes[hypo][data] -= prob

    mixes = {
        'Bowl1': { 'vanilla': 30, 'chocolate': 10 },
        'Bowl2': { 'vanilla': 20, 'chocolate': 20 }
    }

    def Likelihood(self, data, hypo):
        mix = self.mixes[hypo]
        like = mix[data] / (mix['vanilla'] + mix['chocolate'])
        return like

    def PrettyPrint(self, title):
        print(f'----{title}----')
        for hypo, prob in self.Items():
            print(hypo, round(prob, 6))

print('------ROUND 1-------')
pmf = Cookie(['Bowl1', 'Bowl2'])
pmf.Update('vanilla')
pmf.PrettyPrint('After 1 runs')
pmf.Update('vanilla')
pmf.PrettyPrint('After 2 runs')
pmf.Update('chocolate')
pmf.PrettyPrint('After chocolate runs')

print('------ROUND 2 WITH REMOVE-------')
pmf2 = Cookie(['Bowl1', 'Bowl2'])
pmf2.UpdateAndRemove('vanilla')
pmf2.PrettyPrint('After 1 run')
pmf2.UpdateAndRemove('vanilla')
pmf2.PrettyPrint('After 2 runs')
pmf2.UpdateAndRemove('chocolate')
pmf2.PrettyPrint('After chocolate runs')


