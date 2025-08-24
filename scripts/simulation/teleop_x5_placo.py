import os

import tyro

from xrobotoolkit_teleop.simulation.placo_teleop_controller import (
    PlacoTeleopController,
)
from xrobotoolkit_teleop.utils.path_utils import ASSET_PATH


def main(
    robot_urdf_path: str = os.path.join(ASSET_PATH, "arx/X5/dual_X5A_EE.urdf"),
    scale_factor: float = 1.5,
):
    """
    Main function to run the X5 teleoperation with Placo.
    """
    config = {
        "right_hand": {
            "link_name": "right_link6",
            "pose_source": "right_controller",
            "control_trigger": "right_grip",
            "vis_target": "right_target",
            "gripper_config": {
                "type": "parallel",
                "gripper_trigger": "right_trigger",
                "joint_names": [
                    "right_joint7",
                ],
                "open_pos": [
                    0.044,
                ],
                "close_pos": [
                    0.0,
                ],
            },
        },
        "left_hand": {
            "link_name": "left_link6",
            "pose_source": "left_controller",
            "control_trigger": "left_grip",
            "vis_target": "left_target",
            "gripper_config": {
                "type": "parallel",
                "gripper_trigger": "left_trigger",
                "joint_names": [
                    "left_joint7",
                ],
                "open_pos": [
                    0.044,
                ],
                "close_pos": [
                    0.0,
                ],
            },
        },
    }

    # Create and initialize the teleoperation controller
    controller = PlacoTeleopController(
        robot_urdf_path=robot_urdf_path,
        manipulator_config=config,
        scale_factor=scale_factor,
    )

    # additional constraints hardcoded here for now
    joints_task = controller.solver.add_joints_task()
    joints_task.set_joints({joint: 0.0 for joint in controller.placo_robot.joint_names()})
    joints_task.configure("joints_regularization", "soft", 5e-4)

    # if "joint2" in controller.placo_robot.joint_names():
    #     controller.placo_robot.set_joint_limits("joint2", -0.5, 0.1)  # to avoid excessive tilting of torso
    #     controller.solver.enable_velocity_limits(True)

    controller.run()


if __name__ == "__main__":
    tyro.cli(main)
