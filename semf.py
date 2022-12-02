import random

class SEMF:
    def __init__(self, p1=None, p2=None):
        if p1 is not None and p2 is not None:
            p1_a_list = [p1.a_V, p1.a_S, p1.a_C, p1.a_A, p1.a_P]
            p2_a_list = [p2.a_V, p2.a_S, p2.a_C, p2.a_A, p2.a_P]
            r = random.randint(0,5)
            a_list = p1_a_list[:r]+p2_a_list[r:]
            self.a_V, self.a_S, self.a_C, self.a_A, self.a_P = a_list
        else:
            self.a_V = random.random()*20
            self.a_S = random.random()*20
            self.a_C = random.random()*20
            self.a_A = random.random()*20
            self.a_P = random.random()*20

    def mutate(self, mu, epsilon):
        a_list = [self.a_V, self.a_S, self.a_C, self.a_A, self.a_P]
        for i in range(len(a_list)): 
            r = random.random()
            if r < mu:
                a_list[i] += random.uniform(-epsilon, epsilon)
        self.a_V, self.a_S, self.a_C, self.a_A, self.a_P = a_list


    def eval(self, N, Z):
        A = N+Z
        volume_term = self.a_V*A
        surface_term = -self.a_S*A**(2/3)
        coulomb_term = -self.a_C*Z**2/A**(1/3)
        asymmetry_term =  -self.a_A*(A-2*Z)**2/A 
        pairing_term = self.a_P/A**(1/2)*((N%2==0 and Z%2==0)-(N%2==1 and Z%2==1))
        B = volume_term+surface_term+coulomb_term+asymmetry_term+pairing_term
        return B

    def loss(self, N, Z, B):
        return (self.eval(N,Z)-B*(N+Z))**2

    def calc_fitness(self, data):
        self.fitness = 0
        for i in range(len(data)):
            n,z,b = data.iloc[i]
            self.fitness -= self.loss(n, z, b)

    def get_self(self):
        return "aV={}, aS={}, aC={}, aA={} and aP={}\n".format(self.a_V, self.a_S, self.a_C, self.a_A, self.a_P)