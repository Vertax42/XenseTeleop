import os

import tyro
from xenseteleop_toolkit.simulation.mujoco_teleop_controller import (
    MujocoTeleopController,
)
from xenseteleop_toolkit.utils.path_utils import ASSET_PATH


def main(
    xml_path: str = os.path.join(ASSET_PATH, "arx/X5/scene.xml"),
    robot_urdf_path: str = os.path.join(ASSET_PATH, "arx/X5/dual_X5A_fixed.urdf"),
    scale_factor: float = 1.5,
    visualize_placo: bool = True,
):
    """
    Main function to run the dual X5A teleoperation in MuJoCo.
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
                    0.05,
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
                    0.05,
                ],
                "close_pos": [
                    0.0,
                ],
            },
        },
    }

    # Create and initialize the teleoperation controller
    controller = MujocoTeleopController(
        xml_path=xml_path,
        robot_urdf_path=robot_urdf_path,
        manipulator_config=config,
        scale_factor=scale_factor,
        visualize_placo=visualize_placo,
    )

    controller.run()


if __name__ == "__main__":
    tyro.cli(main)
