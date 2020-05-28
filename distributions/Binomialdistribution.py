import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """      
       
    def __init__(self, prob = 0.5, size =20):
        
        self.p = prob
        self.n = size
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
                
    def calculate_mean(self):
         
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mu = self.p*self.n
        return self.mu
         

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.sigma = math.sqrt(self.n* self.p * (1 - self.p))
        return self.sigma
        
        
    def replace_stats_with_data(self):
          
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
                     
        self.n = len(self.data)
        self.p = sum(self.data)/self.n
        self.mean = self.calculate_mean()
        self.sigma = self.calculate_mean()
        return self.p, self.n
        
       
    def plot_bar(self):
    
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.dataset)
        plt.title('Histogram of Bionomial Data')
        plt.xlabel('data')
        plt.ylabel('count')
        
        
    def binomial_pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        binomial_func = (math.factorial(self.n)/(math.factorial(self.n-k)*math.factorial(k)))*(self.p**k)*((1-self.p)**(self.n-k))
        return binomial_func
    
        
    def binomial_pdf_plot(self):
    
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        
        x = []
        y = []

        # calculate the x values to visualize
        for i in range(self.size+1):
            x.append(i)
            y.append(self.binomial_pdf(tmp))

            # make the plots
            fig, axes = plt.subplots(2,sharex=True)
            fig.subplots_adjust(hspace=.5)
            axes[0].hist(self.data, density=True)
            axes[0].set_title('Binomial Histogram of Data')
            axes[0].set_ylabel('Density')

            axes[1].plot(x, y)
            axes[1].set_title('Binomial Distribution for \n Sample Mean and Sample Standard Deviation')
            axes[0].set_ylabel('Density')
            plt.show()

            return x, y
        
        
        
    def __add__(self,other):            
            
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p =self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result
 


    def __repr__ (self):
        
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
        return "mean {}, standard deviation {}, p {}, n {}".format(self.mean, self.stdev, self.p, self.n)
