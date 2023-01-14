from matplotlib import pyplot as plt
import sys
#experiment_name = 'freeze-rate'

def find_substring_end_index(string, token):
    start_index = string.find(token)
    if start_index == -1:
        return -1
    else:
        return start_index + len(token) - 1


def read_loss(experiment_name):
    res = []
    with open("/root/autodl-tmp/pytorch-CycleGAN-and-pix2pix/checkpoints/" + experiment_name + "/loss_log.txt", "r") as f:
        for i in f:
            if i[0] != "=":
                loss_dict = {}.fromkeys(["D_A", "G_A", "cycle_A", "idt_A", "D_B", "G_B", "cycle_B", "idt_B"])
                loss_dict["D_A"] = i[find_substring_end_index(i, "D_A") + 2:find_substring_end_index(i, "D_A") + 8]
                loss_dict["G_A"] = i[find_substring_end_index(i, "G_A") + 2:find_substring_end_index(i, "G_A") + 8]
                loss_dict["cycle_A"] = i[find_substring_end_index(i, "cycle_A") + 2:find_substring_end_index(i, "cycle_A") + 8]
                loss_dict["idt_A"] = i[find_substring_end_index(i, "idt_A") + 2:find_substring_end_index(i, "idt_A") + 8]
                loss_dict["D_B"] = i[find_substring_end_index(i, "D_B") + 2:find_substring_end_index(i, "D_B") + 8]
                loss_dict["G_B"] = i[find_substring_end_index(i, "G_B") + 2:find_substring_end_index(i, "G_B") + 8]
                loss_dict["cycle_B"] = i[find_substring_end_index(i, "cycle_B") + 2:find_substring_end_index(i, "cycle_B") + 8]
                loss_dict["idt_B"] = i[find_substring_end_index(i, "idt_B") + 2:find_substring_end_index(i, "idt_B") + 8]
                res.append(loss_dict)
            
    return res


#def plot_loss(res):

def plot_multiple_curves(data_list, experiment_name):
    x = list(range(1, len(data_list)+1))
    plt.plot(x, [float(data_list[i]['D_A']) for i in range(len(data_list))], label='D_A')
    plt.plot(x, [float(data_list[i]['G_A']) for i in range(len(data_list))], label='G_A')
    plt.plot(x, [float(data_list[i]['cycle_A']) for i in range(len(data_list))], label='cycle_A')
    plt.plot(x, [float(data_list[i]['idt_A']) for i in range(len(data_list))], label='idt_A')
    plt.plot(x, [float(data_list[i]['D_B']) for i in range(len(data_list))], label='D_B')
    plt.plot(x, [float(data_list[i]['G_B']) for i in range(len(data_list))], label='G_B')
    plt.plot(x, [float(data_list[i]['cycle_B']) for i in range(len(data_list))], label='cycle_B')
    plt.plot(x, [float(data_list[i]['idt_B']) for i in range(len(data_list))], label='idt_B')

    plt.xticks(range(1, len(data_list)+1, 20))
    plt.xlabel('No. of epochs')
    plt.ylabel('Loss')
    plt.title('Learning curve of the style transfer model on horse')
    plt.legend(bbox_to_anchor=(1, 1,), loc='upper left') # bbox_to_anchor=(1, 1,)
    plt.savefig('log/loss_' + experiment_name + '.png', bbox_inches='tight') #  bbox_inches='tight'
    #plt.show()
    

if __name__ == '__main__':
    #experiment_name = 'freeze-finetune'
    experiment_name = sys.argv[1]
    res = read_loss(experiment_name)
    # print(res)
    plot_multiple_curves(res, experiment_name)
    
