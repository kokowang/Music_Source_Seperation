import torch
import torch.nn as nn
import torchvision.datasets as datasets
import torch.nn.functional as F
import torch.optim as optim
from IPython import display
import matplotlib.pyplot as plt
import numpy as np
from time import time
import os
import shutil

feature_maps = 3*4

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        self.conv0 = nn.Conv2d(4, feature_maps, 7, padding=3)
        self.conv0_bn = nn.BatchNorm2d(feature_maps)
        self.conv1 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)
        self.conv1_bn = nn.BatchNorm2d(feature_maps)
        self.conv2 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv2_bn = nn.BatchNorm2d(feature_maps)
        self.conv3 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv3_bn = nn.BatchNorm2d(feature_maps)
        self.conv4 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv4_bn = nn.BatchNorm2d(feature_maps)
        self.conv5 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1) 
        self.conv5_bn = nn.BatchNorm2d(feature_maps) 
        self.conv6 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv6_bn = nn.BatchNorm2d(feature_maps)
        self.conv7 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv7_bn = nn.BatchNorm2d(feature_maps)
        self.conv8 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv8_bn = nn.BatchNorm2d(feature_maps)
        self.conv9 = nn.Conv2d(feature_maps, feature_maps, 3, padding=1)  
        self.conv9_bn = nn.BatchNorm2d(feature_maps)
        self.conv10 = nn.Conv2d(feature_maps, feature_maps*2, 3, padding=1) 
        self.conv10_bn = nn.BatchNorm2d(feature_maps*2) 
        self.conv11 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv11_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv12 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv12_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv13 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv13_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv14 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv14_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv15 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv15_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv16 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv16_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv17 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv17_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv18 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv18_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv19 = nn.Conv2d(feature_maps*2, feature_maps*2, 3, padding=1)  
        self.conv19_bn = nn.BatchNorm2d(feature_maps*2)
        self.conv20 = nn.Conv2d(feature_maps*2, feature_maps*4, 3, padding=1) 
        self.conv20_bn = nn.BatchNorm2d(feature_maps*4) 
        self.conv21 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv21_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv22 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv22_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv23 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv23_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv24 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv24_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv25 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv25_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv26 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv26_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv27 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv27_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv28 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv28_bn = nn.BatchNorm2d(feature_maps*4)
        self.conv29 = nn.Conv2d(feature_maps*4, feature_maps*4, 3, padding=1)  
        self.conv29_bn = nn.BatchNorm2d(feature_maps*4)

        self.conv30 = nn.Conv2d(feature_maps*4, 4, 3, padding=1)  
        self.conv30_bn = nn.BatchNorm2d(4)
        self.fc1 = nn.Linear(4100, 4100)
        self.fc2 = nn.Linear(1000, 4100)

    def forward(self, x):

        res = x
        for a in range(feature_maps//4 - 1):
            res = torch.cat([res,x], 1)
        x = F.leaky_relu(self.conv0(x))
        x = self.conv0_bn(x)

        x = F.leaky_relu(self.conv1(x))
        x = self.conv1_bn(x)
        x = res + x
        
        res = x
        x = F.leaky_relu(self.conv2(x))
        x = self.conv2_bn(x)

        x = F.leaky_relu(self.conv3(x))
        x = self.conv3_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv4(x))
        x = self.conv4_bn(x)

        x = F.leaky_relu(self.conv5(x))
        x = self.conv5_bn(x)
        x = res + x
        
        res = x
        x = F.leaky_relu(self.conv6(x))
        x = self.conv6_bn(x)

        x = F.leaky_relu(self.conv7(x))
        x = self.conv7_bn(x)
        x = res + x
        
        res = x
        x = F.leaky_relu(self.conv8(x))
        x = self.conv8_bn(x)

        x = F.leaky_relu(self.conv9(x))
        x = self.conv9_bn(x)
        x = res + x

        res = torch.cat([x[:,:,:,10:15],x[:,:,:,10:15]],1)
        x = F.max_pool2d(F.leaky_relu(self.conv10(x)), (1, 5))
        x = self.conv10_bn(x)

        x = F.leaky_relu(self.conv11(x))
        x = self.conv11_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv12(x))
        x = self.conv12_bn(x)

        x = F.leaky_relu(self.conv13(x))
        x = self.conv13_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv14(x))
        x = self.conv14_bn(x)

        x = F.leaky_relu(self.conv15(x))
        x = self.conv15_bn(x)
        x = res + x
        
        res = x
        x = F.leaky_relu(self.conv16(x))
        x = self.conv16_bn(x)

        x = F.leaky_relu(self.conv17(x))
        x = self.conv17_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv18(x))
        x = self.conv18_bn(x)

        x = F.leaky_relu(self.conv19(x))
        x = self.conv19_bn(x)
        x = res + x

        res = torch.cat([x,x],1)
        x = F.max_pool2d(F.leaky_relu(self.conv20(x)), (1, 5))
        x = self.conv20_bn(x)

        x = F.leaky_relu(self.conv21(x))
        x = self.conv21_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv22(x))
        x = self.conv22_bn(x)

        x = F.leaky_relu(self.conv23(x))
        x = self.conv23_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv24(x))
        x = self.conv24_bn(x)

        x = F.leaky_relu(self.conv25(x))
        x = self.conv25_bn(x)
        x = res + x
        
        res = x
        x = F.leaky_relu(self.conv26(x))
        x = self.conv26_bn(x)

        x = F.leaky_relu(self.conv27(x))
        x = self.conv27_bn(x)
        x = res + x

        res = x
        x = F.leaky_relu(self.conv28(x))
        x = self.conv28_bn(x)

        x = F.leaky_relu(self.conv29(x))
        x = self.conv29_bn(x)
        x = res + x
        
        res = torch.zeros_like(x[:,0:4,:,2:3])
        for a in range(4):
            res[:,a] = torch.mean(x[:,a*2*feature_maps//4:(a+1)*2*feature_maps//4,:,2:3], 1)
        # res[:,0] = torch.mean(x[:,0:16,:,2:3], 1)
        # res[:,1] = torch.mean(x[:,16:32,:,2:3], 1)
        # res[:,2] = torch.mean(x[:,32:48,:,2:3], 1)
        # res[:,3] = torch.mean(x[:,48:64,:,2:3], 1)
        x = F.avg_pool2d(F.leaky_relu(self.conv30(x)), (1, 5))
        x = self.conv30_bn(x)
        x = res + x

        return x

        shape = x.shape    
        x = x.view(-1, self.num_flat_features(x)) 

        x = self.fc1(x)
        #x = self.fc2(x)

        x = x.view(shape)

        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


class LogCoshLoss(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, y_t, y_prime_t):
        loss = torch.mean(torch.cosh(torch.log(torch.abs(y_t - y_prime_t)+1)))
        return loss


def confusion(pred, exp):
    correct=0
    ids=[]
    length = len(exp[0])
    confusion = np.zeros((length,length))
    for i in range(len(pred)):
        p = np.matrix(pred[i])
        e = np.matrix(exp[i])
        confusion += np.dot(p.T, e)
        if(np.array_equal(p,e)):
            correct += 1
        else:
            ids.append(i)
    print(confusion)
    return (correct/len(pred) * 100), ids

def learn(net, optim, data, target, batch_size=10):
    device = torch.device("cuda:0" if (next(net.parameters()).is_cuda) else "cpu")
    losses = []
    calc = LogCoshLoss().to(device)
    net.train()
    plt.ion()
    for batch in range(np.int(np.floor(len(data)/batch_size))):
        X = data[batch*batch_size:(batch+1)*batch_size].to(device)
        y = target[batch*batch_size:(batch+1)*batch_size].to(device)

        net.zero_grad()
        output = net(X)
        loss = calc(output, y)
        loss.backward()
        
        optim.step()

        losses.append(loss.item())
        
        if(batch%20==0):
            plot_train(losses)

    return np.mean(losses)


# def learn(net, optimizer, X, y, batch_size = 50):
#     torch.backends.cudnn.fastest = True
#     calc = LogCoshLoss().cuda()
#     totalloss=0
#     indicies = torch.randperm(len(X))
#     for batch in range(np.int(np.floor(len(X)/batch_size))):
#             optimizer.zero_grad()
#             tx = X[indicies[batch*batch_size:(batch+1)*batch_size]].cuda()
#             ty = y[indicies[batch*batch_size:(batch+1)*batch_size]].cuda()
#             pred = net(tx)
#             loss = calc(pred, ty)
#             totalloss += loss.detach()
#             loss.backward()
#             optimizer.step()
#             #print(batch*batch_size / samples * 100, "%")

#     losses = totalloss/np.int(np.floor(X.size(0)/batch_size)) * y.size(1)
#     return losses.item()

def test(net, data, target, batch_size=10):
    device = torch.device("cuda:0" if (next(net.parameters()).is_cuda) else "cpu")
    losses = []
    calc = LogCoshLoss().to(device)
    net.eval()

    for batch in range(np.int(np.floor(len(data)/batch_size))):
        X = data[batch*batch_size:(batch+1)*batch_size].to(device)
        y = target[batch*batch_size:(batch+1)*batch_size].to(device)

        output = net(X)
        loss = calc(output, y).detach()

        losses.append(loss.item())

    return np.mean(losses)

# def test(model, X, y, batch_size=50):

#     calc = LogCoshLoss().cuda()
#     model.eval()
#     indicies = torch.randperm(len(X))
#     pred = torch.zeros_like(y).cuda()

#     for batch in range(np.int(np.floor(len(X)/batch_size))):
#         tx = X[indicies[batch*batch_size:(batch+1)*batch_size]]
#         pred[indicies[batch*batch_size:(batch+1)*batch_size]] = model(tx.cuda()).detach()
    
#     loss = calc(pred,y.cuda()).detach().cpu().numpy() * y.size(1)
#     return loss


def plot_train(trainloss, testloss=None):
    plt.clf()
    plt.plot(np.linspace(2,len(trainloss),len(trainloss)-1), trainloss[1:], label="train")
    if testloss is not None:
        plt.plot(np.linspace(2,len(testloss),len(testloss)-1), testloss[1:], label="test")
    plt.legend()
    plt.xlabel('epoch')
    plt.ylabel('loss') 
    display.display(plt.gcf())
    display.clear_output(wait=True)

def train(net, optim, data, target, batch_size=10, validation_size=None, epochs=1):

    if validation_size is None:
        validation_size = data.size(0) // 10

    #Scrambling data for training
    ind = np.random.permutation(data.size(0))

    #Splitting data to train and validation
    validationX = data[ind[:validation_size]]
    validationy = target[ind[:validation_size]]
    trainX = data[ind[validation_size:]]
    trainy = target[ind[validation_size:]]

    #Training
    print("Starting Training:")
    train_loss = []
    validation_loss = []
    plt.ion()
    start = time()
    epoch = 0

    for i in range(epochs):
        loss = learn(net, optim, trainX, trainy, batch_size=batch_size)
        train_loss.append(loss)

        loss = test(net, validationX, validationy, batch_size=batch_size)
        validation_loss.append(loss)

        elapsed = time() - start

        print("Epoch:", i+1)
        print("Train loss:", train_loss[i])
        print("validation loss:", validation_loss[i])
        print("Time:", elapsed)
        # plot_train(train_lossD, train_lossG, train_realD, validation_lossD, validation_lossG, validation_realD)
        epoch += 1

# def train(model, optimizer, X, y, validation_size, batch_size=100, epochs=1):

#     #Scrambling data for training
#     ind = np.random.permutation(len(y))

#     #Splitting data to train and validation
#     validationX = X[ind[:validation_size]]
#     validationy = y[ind[:validation_size]]
#     trainX = X[ind[validation_size:]]
#     trainy = y[ind[validation_size:]]

#     #Training
#     print("Starting Training:")
#     trainloss = []
#     validation_loss = []
#     plt.ion()
#     start = time()
#     epoch = 0

#     for i in range(epochs):
#         trainloss.append(learn(model, optimizer, trainX, trainy, batch_size=batch_size))
#         elapsed = time() - start
#         loss = test(model, validationX, validationy, batch_size=batch_size)
#         validation_loss.append(loss)
#         print("Epoch:", i+1)
#         print("Train loss:", trainloss[i])
#         print("validation loss:", validation_loss[i])
#         print("Time:", elapsed)
#         plot_train(trainloss,validation_loss)
#         epoch += 1


def save_checkpoint(state, is_best, filename='checkpoint.pth.tar'):
    torch.save(state, filename)
    if is_best:
        shutil.copyfile(filename, 'model_best.pth.tar')


def load_checkpoint(model, optimizer, filename='checkpoint.pth.tar'):
    if os.path.isfile(filename):
        print("=> loading checkpoint '{}'".format(filename))
        checkpoint = torch.load(filename)
        start_epoch = checkpoint['epoch']
        best_prec1 = checkpoint['best_prec1']
        model.load_state_dict(checkpoint['state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer'])
        print("=> loaded checkpoint '{}' (epoch {})"
                .format(filename, checkpoint['epoch']))
        return start_epoch, best_prec1
    else:
        print("=> no checkpoint found at '{}'".format(filename))