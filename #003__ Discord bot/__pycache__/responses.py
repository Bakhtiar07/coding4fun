�
    �'f6	  �                   �>   � d dl mZmZ d dlZdedefd�Zdedefd�ZdS )�    )�choice�randintN�
user_input�returnc                 �  � | �                     �   �         }|dk    rdS d|v rdS d|v rdS d|v rdt          d	d
�  �        � �S d|v sd|v sd|v rt          g d��  �        S d|v sd|v sd|v rt          ddg�  �        S d|v sd|v sd|v rt          g d��  �        S d|v sd|v sd|v rt          g d��  �        S t          ddg�  �        S )N� zWell, you're awfully silent...�hellozHello there!zhow are youzUp and running!z	roll dicezYou rolled: �   �   zyou're awesomezlove youzyou're great)zOh, you're making me blush!z'Thanks, you're pretty awesome yourself!zI appreciate that!ztell me a jokezmake me laugh�jokezBWhy don't scientists trust atoms? Because they make up everything!zqI told my computer I needed a break, and it said 'You seem to be working hard, try chilling with some ice-cream!'zi'm feeling downzneed some motivationzcheer me up)z+Keep your head up. Tomorrow is another day!z5You're doing great, don't forget how far you've come!z.Every day is a second chance. You've got this!ztell me a factzgive me a factzrandom fact)z.Did you know that octopuses have three hearts?z�Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old but still perfectly edible!z/A group of flamingos is called a 'flamboyance'.zI'm afraid I do not follow...zCan you rephrase that?)�lowerr   r   )r   �lowereds     �Dc:\Users\Bakhtiar\Desktop\coding4fun\#003__ Discord bot\responses.py�get_responser      s�  � ��#�#�%�%�G��"�}�}�0�0�	�G�	�	��~�	�'�	!�	!� � �	��	�	�,�g�a��l�l�,�,�,�	�g�	%�	%��w�)>�)>�/�U\�B\�B\��v�v�v�w�w�w�	�W�	$�	$��7�(B�(B�f�PW�FW�FW��[� G�H� I� I� 	I�	�w�	&�	&�*@�G�*K�*K�}�`g�Og�Og�� E� E� E� F� F� 	F� 
�W�	$�	$�(8�G�(C�(C�}�X_�G_�G_�� F� F� F� G� G� 	G� �7�/�1� 2� 2� 	2�    �durationc              �   �X   K  � d| � d�}t          j        | dz  �  �        � d {V �� d}||fS )NzTimer started for z minutes. Time to focus!�<   z7Time's up! Take a short break before your next session.)�asyncio�sleep)r   �start_message�end_messages      r   �start_timerr   %   sQ   � � � �K��K�K�K�M� �-��2��
&�
&�&�&�&�&�&�&�&� L�K��+�%�%r   )�randomr   r   r   �strr   �intr   � r   r   �<module>r      su   �� "� "� "� "� "� "� "� "� ����2�S� 2�S� 2� 2� 2� 2�B
&�� 
&�� 
&� 
&� 
&� 
&� 
&� 
&r   