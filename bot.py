ó
ª©^c           @   s;   d  d l  Z  d  d l Z d  d l Z d d d     YZ d S(   iÿÿÿÿNt   telegram_chatbotc           B   s/   e  Z d    Z d d  Z d   Z d   Z RS(   c         C   s+   |  j  |  |  _ d j |  j  |  _ d  S(   Ns   https://api.telegram.org/bot{}/(   t   read_token_from_config_filet   tokent   formatt   base(   t   selft   config(    (    s&   /home/osiris/Application/Qoutes/bot.pyt   __init__	   s    c         C   sL   |  j  d } | r- | d j | d  } n  t j |  } t j | j  S(   Ns   getUpdates?timeout=100s
   &offset={}i   (   R   R   t   requestst   gett   jsont   loadst   content(   R   t   offsett   urlt   r(    (    s&   /home/osiris/Application/Qoutes/bot.pyt   get_updates   s
    c         C   s9   |  j  d j | |  } | d  k	 r5 t j |  n  d  S(   Ns   sendMessage?chat_id={}&text={}(   R   R   t   NoneR   R	   (   R   t   msgt   chat_idR   (    (    s&   /home/osiris/Application/Qoutes/bot.pyt   send_message   s    c         C   s)   t  j   } | j |  | j d d  S(   Nt   credsR   (   t   cfgt   ConfigParsert   readR	   (   R   R   t   parser(    (    s&   /home/osiris/Application/Qoutes/bot.pyR      s    N(   t   __name__t
   __module__R   R   R   R   R   (    (    (    s&   /home/osiris/Application/Qoutes/bot.pyR       s   		(    (   R   R
   t   configparserR   R    (    (    (    s&   /home/osiris/Application/Qoutes/bot.pyt   <module>   s   