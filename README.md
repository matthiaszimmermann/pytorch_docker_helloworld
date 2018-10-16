# PyTorch "Hello world" using Docker

Repo to show how to work with PyTorch using a simple Docker image. To check if PyTorch works as intended the first steps of a simple [PyTorch Tutorial](https://pytorch.org/tutorials/beginner/nlp/deep_learning_tutorial.html) are replicated.

* ```helloworld.py```: Import torch and call some functions
* ```bow.py```: Toy "bag of words" model to classify English and Spanish texts

## PyTorch Docker Image

Use the [anibali/docker-pytorch](https://github.com/anibali/docker-pytorch) Docker Image. Only the 'no-cuda' version was used for testing. To get the image you may use the following command.

```
docker pull anibali/pytorch:no-cuda
```

## Run the "Hello World"

To run script ```helloworld.py``` you may use the following command.

```
docker run --rm --volume=$PWD:/app anibali/pytorch:no-cuda python3 helloworld.py
```

Parameter description
* ```-rm```: Removes container after running it
* ```--volume=$PWD:/app```: Mounts the current directory (```$PWD``` outside of the container) to path ```/app``` inside the container
* ```anibali/pytorch:no-cuda```: Starts the PyTorch container
* ```python3 helloworld.py```: Runs the script ```helloworld.py``` insided the container (where PyTorch is available)

This works as the ```anibali/pytorch``` container sets directory ```/app``` as working directory of the container. as we mount the current directory (with the script ```helloworld.py```) into this ```/app``` directory. The makes the script directly visible for execution. The expected output is shown below.

```
tensor([[ 0.1755, -0.3268, -0.5069],
        [-0.6602,  0.2260,  0.1089]], grad_fn=<ThAddmmBackward>)
tensor([[-0.5404, -2.2102],
        [ 2.1130, -0.0040]])
tensor([[0.0000, 0.0000],
        [2.1130, 0.0000]])
tensor([ 1.3800, -1.3505,  0.3455,  0.5046,  1.8213])
tensor([0.2948, 0.0192, 0.1048, 0.1228, 0.4584])
tensor(1.)
tensor([-1.2214, -3.9519, -2.2560, -2.0969, -0.7801])
```

## Run the "Bag of Words" Script

To run script ```bow.py``` you may use the following command.

```
docker run --rm --volume=$PWD:/app anibali/pytorch:no-cuda python3 bow.py
```

The expected output is shown below.

```
{'me': 0, 'gusta': 1, 'comer': 2, 'en': 3, 'la': 4, 'cafeteria': 5, 'Give': 6, 'it': 7, 'to': 8, 'No': 9, 'creo': 10, 'que': 11, 'sea': 12, 'una': 13, 'buena': 14, 'idea': 15, 'is': 16, 'not': 17, 'a': 18, 'good': 19, 'get': 20, 'lost': 21, 'at': 22, 'Yo': 23, 'si': 24, 'on': 25}
Parameter containing:
tensor([[ 0.1011, -0.0866, -0.0380,  0.0921, -0.1846,  0.1176, -0.0403,  0.0998,
          0.0273, -0.0240,  0.0544,  0.0097,  0.0716, -0.0764, -0.0143, -0.0177,
          0.0284, -0.0008,  0.1714,  0.0610, -0.0730, -0.1184, -0.0329, -0.0846,
         -0.0628,  0.0094],
        [ 0.1169,  0.1066, -0.1917,  0.1216,  0.0548,  0.1860,  0.1294, -0.1787,
         -0.1865, -0.0946,  0.1722, -0.0327,  0.0839, -0.0911,  0.1924, -0.0830,
          0.1471,  0.0023, -0.1033,  0.1008, -0.1041,  0.0577, -0.0566, -0.0215,
         -0.1885, -0.0935]], requires_grad=True)
Parameter containing:
tensor([ 0.1064, -0.0477], requires_grad=True)
tensor([[-0.8195, -0.5810]])
tensor([[-0.6250, -0.7662]])
tensor([[-0.5870, -0.8119]])
tensor([0.0544, 0.1722], grad_fn=<SelectBackward>)
tensor([[-0.1210, -2.1721]])
tensor([[-2.7767, -0.0643]])
tensor([ 0.5004, -0.2738], grad_fn=<SelectBackward>)
```




